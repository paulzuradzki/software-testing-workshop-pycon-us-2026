"""Exercise 2.2: Integration test for ToDoTracker.

Goal: write a single test that exercises more than one method together
(create + read), verifying the methods cooperate as expected. Compare
with 2.1, where each test pinned down one method in isolation.

Run from the repo root:

    pytest modules/2.2_integration_test_todotracker -q
"""
from todo import ToDoTracker, ToDo


def test_create_and_search_todos():
    # Arrange
    todo_tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)

    # Act
    # TODO: create the todo, then call read_todos() to fetch the full list

    # Assert
    # TODO: assert the created todo equals expected_todo
    # TODO: assert read_todos() returns a list containing only expected_todo
    raise AssertionError("TODO: replace this with the real Act and Assert steps")
