"""Solution for Exercise 2.4 (file fixture and update_todo).

Implements FileToDoTracker.update_todo (in this directory's todo.py)
and tests it with the file_tracker fixture. Two assertions per test:
the on-disk JSON and the in-memory tracker view, plus a reload check
that proves persistence survives a fresh tracker.
"""
import json

import pytest

from todo import FileToDoTracker, ToDo


@pytest.fixture
def file_tracker(tmp_path):
    return FileToDoTracker(tmp_path / "todo_tracker.json")


def test_update_todo_persists_to_file(file_tracker):
    # Arrange
    original = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    file_tracker.create_todo(original)
    replacement = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=True)

    # Act
    file_tracker.update_todo(0, replacement)

    # Assert: on-disk JSON reflects the update.
    on_disk = json.loads(file_tracker.path.read_text())
    assert on_disk == [replacement.to_dict()]
    # Assert: tracker memory matches what is on disk.
    assert file_tracker.read_todos() == [replacement]


def test_update_todo_survives_reload(file_tracker):
    # Arrange
    original = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    file_tracker.create_todo(original)
    replacement = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=True)
    file_tracker.update_todo(0, replacement)

    # Act: a fresh tracker pointed at the same file should rehydrate state.
    reloaded = FileToDoTracker(file_tracker.path)

    # Assert
    assert reloaded.read_todos() == [replacement]
