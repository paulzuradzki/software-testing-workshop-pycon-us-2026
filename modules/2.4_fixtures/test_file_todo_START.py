"""Exercise 2.4: file fixture and the missing method.

Two parts:

  1. In todo.py, implement FileToDoTracker.update_todo. Replace the
     todo at the given index and persist the change to disk. Look at
     delete_todo for the pattern.
  2. Fill in the two test bodies below. Use the file_tracker fixture
     and assert at two layers: tracker state and the JSON file on
     disk.

The pytest demo at test_file_todo_DEMO.py applies the same fixture
shape to create_todo. Compare the two files side by side.
"""
import json

import pytest

from todo import FileToDoTracker, ToDo


@pytest.fixture
def file_tracker(tmp_path):
    """Fresh FileToDoTracker per test. tmp_path supplies the location
    and pytest removes it after the test."""
    return FileToDoTracker(tmp_path / "todo_tracker.json")


def test_update_todo_persists_to_file(file_tracker):
    # Arrange: create a todo so there is something to update.
    # TODO(student): build a ToDo and call file_tracker.create_todo(...)

    # Act: update it.
    # TODO(student): build a replacement ToDo and call
    #                file_tracker.update_todo(index, replacement)

    # Assert: the JSON on disk reflects the update.
    # TODO(student): json.loads(file_tracker.path.read_text()) and
    #                compare against the replacement's to_dict().
    raise AssertionError("replace this with the real assertions")


def test_update_todo_survives_reload(file_tracker):
    # Arrange + Act: same flow as above, then re-open the file with a
    # fresh FileToDoTracker.
    # TODO(student): create, update, then build a new tracker pointed
    #                at file_tracker.path and assert read_todos()
    #                returns the updated todo.
    raise AssertionError("replace this with the real assertions")


# Side quest (optional, for fast finishers): same exercise against a
# SQLite-backed tracker. Build a SqliteToDoTracker with the same six
# methods, open sqlite3.connect(":memory:") in a fixture, yield the
# tracker, and close the connection on teardown. A real deployment
# would pass a file path instead of ":memory:".
