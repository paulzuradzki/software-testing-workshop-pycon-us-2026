"""Solution for Exercise 2.1 (Unit tests for ToDoTracker).

Imports `todo` from the corresponding modules/ directory via conftest.py.
"""
from todo import ToDoTracker, ToDo


def test_create_todo():
    # Arrange
    todo_tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    # Act
    created_todo = todo_tracker.create_todo(expected_todo)
    # Assert
    assert created_todo == expected_todo
    assert len(todo_tracker.todos) == 1
    assert todo_tracker.todos[0] == expected_todo


def test_search_todos():
    # Arrange
    todo_tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    todo_tracker.create_todo(expected_todo)
    # Act
    found_todos = todo_tracker.search_todos("groceries")
    # Assert
    assert found_todos == [expected_todo]
