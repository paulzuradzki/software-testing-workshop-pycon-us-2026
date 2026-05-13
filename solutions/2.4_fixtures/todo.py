"""Solution version of 2.4 todo.py.

Same as modules/2.4_fixtures/todo.py with FileToDoTracker.update_todo
implemented, plus SqliteToDoTracker for the optional side quest. The
conftest in this directory makes `from todo import ...` resolve to
this file rather than the modules copy.
"""

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class ToDo:
    id: int
    title: str
    description: str
    completed: bool

    def to_dict(self):
        """Convert ToDo instance to a dictionary for JSON serialization."""
        return asdict(self)


class ToDoTracker:
    """In-memory tracker. Same shape as 2.1/2.2. No persistence."""

    def __init__(self):
        self.todos: list[ToDo] = []

    def create_todo(self, todo: ToDo):
        self.todos.append(todo)
        return todo

    def read_todos(self):
        return self.todos

    def get_todo(self, index: int):
        return self.todos[index]

    def search_todos(self, query: str):
        return [todo for todo in self.todos if query in todo.title or query in todo.description]

    def update_todo(self, index: int, new_todo: ToDo):
        self.todos[index] = new_todo

    def delete_todo(self, index: int):
        self.todos.pop(index)


class FileToDoTracker:
    """Persists todos to a JSON file. Each mutation rewrites the file.

    Same six-method surface as ToDoTracker. Any caller that uses these
    method names can switch between in-memory and file-backed storage
    with no other change.
    """

    def __init__(self, path):
        self.path = Path(path)
        if self.path.exists():
            raw = self.path.read_text() or "[]"
            self.todos: list[ToDo] = [ToDo(**item) for item in json.loads(raw)]
        else:
            self.todos = []
            self._save()

    def _save(self):
        self.path.write_text(json.dumps([todo.to_dict() for todo in self.todos]))

    def create_todo(self, todo: ToDo):
        self.todos.append(todo)
        self._save()
        return todo

    def read_todos(self):
        return list(self.todos)

    def get_todo(self, index: int):
        return self.todos[index]

    def search_todos(self, query: str):
        return [todo for todo in self.todos if query in todo.title or query in todo.description]

    def update_todo(self, index: int, new_todo: ToDo):
        self.todos[index] = new_todo
        self._save()

    def delete_todo(self, index: int):
        self.todos.pop(index)
        self._save()


class SqliteToDoTracker:
    """Persists todos to a SQLite database via a caller-supplied connection.

    Same six-method surface as ToDoTracker and FileToDoTracker. Tests
    pass a `sqlite3.connect(":memory:")` connection; a production
    deployment would pass `sqlite3.connect("/path/to/db.sqlite")`.
    The tracker does not own the connection's lifecycle. The fixture
    or caller opens and closes it.

    Order of todos follows insertion order via SQLite's implicit rowid.
    """

    def __init__(self, connection):
        self.conn = connection
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS todos ("
            " id INTEGER, title TEXT, description TEXT, completed INTEGER)"
        )

    def _row_to_todo(self, row):
        return ToDo(id=row[0], title=row[1], description=row[2], completed=bool(row[3]))

    def create_todo(self, todo: ToDo):
        self.conn.execute(
            "INSERT INTO todos (id, title, description, completed) VALUES (?, ?, ?, ?)",
            (todo.id, todo.title, todo.description, int(todo.completed)),
        )
        self.conn.commit()
        return todo

    def read_todos(self):
        cursor = self.conn.execute(
            "SELECT id, title, description, completed FROM todos ORDER BY rowid"
        )
        return [self._row_to_todo(r) for r in cursor.fetchall()]

    def get_todo(self, index: int):
        cursor = self.conn.execute(
            "SELECT id, title, description, completed FROM todos ORDER BY rowid LIMIT 1 OFFSET ?",
            (index,),
        )
        row = cursor.fetchone()
        if row is None:
            raise IndexError(index)
        return self._row_to_todo(row)

    def search_todos(self, query: str):
        pattern = f"%{query}%"
        cursor = self.conn.execute(
            "SELECT id, title, description, completed FROM todos "
            "WHERE title LIKE ? OR description LIKE ? ORDER BY rowid",
            (pattern, pattern),
        )
        return [self._row_to_todo(r) for r in cursor.fetchall()]

    def update_todo(self, index: int, new_todo: ToDo):
        rowid = self._rowid_at(index)
        self.conn.execute(
            "UPDATE todos SET id=?, title=?, description=?, completed=? WHERE rowid=?",
            (new_todo.id, new_todo.title, new_todo.description, int(new_todo.completed), rowid),
        )
        self.conn.commit()

    def delete_todo(self, index: int):
        rowid = self._rowid_at(index)
        self.conn.execute("DELETE FROM todos WHERE rowid=?", (rowid,))
        self.conn.commit()

    def _rowid_at(self, index: int):
        cursor = self.conn.execute(
            "SELECT rowid FROM todos ORDER BY rowid LIMIT 1 OFFSET ?", (index,)
        )
        row = cursor.fetchone()
        if row is None:
            raise IndexError(index)
        return row[0]
