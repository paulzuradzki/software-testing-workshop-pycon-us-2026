"""
Same scenario as the unittest version, expressed as pytest fixtures.

Two flavors are shown side by side:

  file_tracker_manual
      A hand-rolled fixture that mirrors setUp / tearDown. Uses tempfile and
      yield. Useful for understanding what tmp_path replaces.

  file_tracker
      The idiomatic version, using pytest's built-in tmp_path fixture.
      Cleanup is automatic. This is what students should reach for in
      practice.

Notice that the test bodies are identical between the two flavors. The
fixture is the only thing that changes.
"""

import json
import tempfile
from pathlib import Path

import pytest
from todo import FileToDoTracker, ToDo


@pytest.fixture
def file_tracker_manual():
    """Hand-rolled equivalent of unittest setUp / tearDown."""
    tmpdir = tempfile.TemporaryDirectory()
    path = Path(tmpdir.name) / "todo_tracker.json"
    yield FileToDoTracker(path)
    tmpdir.cleanup()


@pytest.fixture
def file_tracker(tmp_path):
    """Idiomatic version using pytest's tmp_path. Cleanup is automatic."""
    return FileToDoTracker(tmp_path / "todo_tracker.json")


def test_create_todo_persists_to_file(file_tracker):
    # Arrange
    todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    # Act
    file_tracker.create_todo(todo)
    # Assert
    on_disk = json.loads(file_tracker.path.read_text())
    assert on_disk == [todo.to_dict()]


def test_create_todo_survives_reload(file_tracker):
    # Arrange
    todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    file_tracker.create_todo(todo)
    # Act
    reloaded = FileToDoTracker(file_tracker.path)
    # Assert
    assert reloaded.read_todos() == [todo]


def test_manual_fixture_produces_the_same_behavior(file_tracker_manual):
    # Same assertion using the hand-rolled fixture. Behavior should match.
    todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    file_tracker_manual.create_todo(todo)
    on_disk = json.loads(file_tracker_manual.path.read_text())
    assert on_disk == [todo.to_dict()]
