"""
Side-by-side starting point: unittest setUp / tearDown.

The system under test (FileToDoTracker) really does persist todos to a JSON
file on disk. That means each test needs:
  - a fresh file location it can own
  - cleanup afterwards so tests don't see each other's leftovers

setUp builds that environment before each test; tearDown takes it back down.
The pytest version of the same demo lives next door in test_file_todo_DEMO.py.
"""
import json
import tempfile
import unittest
from pathlib import Path

from todo import FileToDoTracker, ToDo


class TestFileToDoTracker(unittest.TestCase):
    def setUp(self):
        """Give each test its own temp directory and a fresh tracker."""
        self._tmpdir = tempfile.TemporaryDirectory()
        self.path = Path(self._tmpdir.name) / "todo_tracker.json"
        self.tracker = FileToDoTracker(self.path)

    def tearDown(self):
        """Remove the temp directory and everything in it."""
        self._tmpdir.cleanup()

    def test_create_todo_persists_to_file(self):
        # Arrange
        todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
        # Act
        self.tracker.create_todo(todo)
        # Assert: the file on disk reflects the mutation
        on_disk = json.loads(self.path.read_text())
        self.assertEqual(on_disk, [todo.to_dict()])

    def test_create_todo_survives_reload(self):
        # Arrange
        todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
        self.tracker.create_todo(todo)
        # Act: a fresh tracker pointed at the same file should rehydrate state
        reloaded = FileToDoTracker(self.path)
        # Assert
        self.assertEqual(reloaded.read_todos(), [todo])
