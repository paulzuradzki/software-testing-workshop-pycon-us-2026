"""Exercise 2.1: Unit tests for ToDoTracker.

Goal: write isolated unit tests for the methods on ToDoTracker.
Treat each test as exercising a single method on a fresh tracker.
Use the AAA pattern (Arrange / Act / Assert).

Run from the repo root:

    pytest modules/2.1_unit_test_todotracker -q
"""

from todo import ToDo, ToDoTracker


def test_create_todo():
    # Arrange
    todo_tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)

    # Act
    # TODO: call create_todo on the tracker and capture the return value

    # Assert
    # TODO: assert the returned todo matches expected_todo
    # TODO: assert the tracker now holds exactly one todo, equal to expected_todo
    raise AssertionError("TODO: replace this with the real Act and Assert steps")


def test_search_todos():
    # Arrange
    # TODO: build a tracker and seed it with one todo whose description contains "groceries"

    # Act
    # TODO: call search_todos with the query "groceries"

    # Assert
    # TODO: assert the result is a list containing the seeded todo
    raise AssertionError("TODO: replace this with the real Arrange/Act/Assert steps")
