import json
import tempfile
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

    Same six-method surface as ToDoTracker. The two are interchangeable
    wherever duck typing is enough: any caller that uses these method
    names can switch between in-memory and file-backed storage with no
    other change.

    The point of this class for the fixtures lesson: it owns a real file
    on disk, so tests have to manage that file's lifecycle. That is what
    fixtures are for.
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
        """Replace the todo at `index` and persist.

        Exercise 2.4: implement this method, then write a test for it
        in test_file_todo_START.py.
        """
        raise NotImplementedError("Exercise 2.4: implement and test this method.")

    def delete_todo(self, index: int):
        self.todos.pop(index)
        self._save()


# Side quest: build SqliteToDoTracker with the same six methods.
# Python's duck typing handles the substitution: any class that
# exposes those methods runs the same tests written against the
# in-memory or file trackers. Start from sqlite3.connect(":memory:")
# for a fast version that needs no temp files.


def main():
    """Manual smoke test: in-memory vs file-backed, same six methods."""
    print("In-memory tracker:")
    mem = ToDoTracker()
    mem.create_todo(ToDo(id=1, title="Buy groceries", description="weekly run", completed=False))
    mem.create_todo(ToDo(id=2, title="Buy fruits", description="bananas + apples", completed=False))
    print(" ", mem.search_todos("groceries"))

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "todos.json"
        print(f"\nFile-backed tracker at {path}:")
        f = FileToDoTracker(path)
        f.create_todo(ToDo(id=1, title="Buy groceries", description="weekly run", completed=False))
        f.create_todo(
            ToDo(id=2, title="Buy fruits", description="bananas + apples", completed=False)
        )
        print(" ", f.search_todos("groceries"))
        print("  raw file contents:", path.read_text())


if __name__ == "__main__":
    main()
