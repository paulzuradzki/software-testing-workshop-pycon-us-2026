"""Solution-side validation for the SQLite side quest.

The fixture/setup/teardown rhythm matches the file-backed tests. The
fixture's job shifts: instead of tmp_path supplying a file location,
the fixture opens a sqlite3 connection and yields a tracker built
around it. Cleanup closes the connection.

The instructor walks through this file (or pivots to it from the
file-backed test) when introducing the "fixtures abstract over
resource ownership" point. Students never see this file in the
student-copy build; the SQLite work lives in the solutions tree only.
"""

import sqlite3

import pytest
from todo import SqliteToDoTracker, ToDo


@pytest.fixture
def sqlite_tracker():
    """Yield a SqliteToDoTracker backed by an in-memory database.

    Production code would pass a path-backed connection
    (sqlite3.connect("/path/to/db.sqlite")). For tests, ":memory:" is
    fast and self-cleaning.
    """
    conn = sqlite3.connect(":memory:")
    yield SqliteToDoTracker(conn)
    conn.close()


def test_create_todo_persists_to_db(sqlite_tracker):
    todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    sqlite_tracker.create_todo(todo)
    assert sqlite_tracker.read_todos() == [todo]


def test_update_todo_persists_to_db(sqlite_tracker):
    original = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    sqlite_tracker.create_todo(original)
    replacement = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=True)

    sqlite_tracker.update_todo(0, replacement)

    assert sqlite_tracker.read_todos() == [replacement]


def test_search_todos_matches_title_and_description(sqlite_tracker):
    sqlite_tracker.create_todo(
        ToDo(id=1, title="Buy groceries", description="weekly", completed=False)
    )
    sqlite_tracker.create_todo(
        ToDo(id=2, title="Walk dog", description="around the block", completed=False)
    )

    matches = sqlite_tracker.search_todos("dog")

    assert [t.id for t in matches] == [2]
