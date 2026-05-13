"""Solution for Exercise 2.2 (Integration test for ToDoTracker).

Imports `todo` from the corresponding modules/ directory via conftest.py.
"""

from todo import ToDo, ToDoTracker


def test_create_and_search_todos():
    # Arrange
    todo_tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    # Act
    created_todo = todo_tracker.create_todo(expected_todo)
    todos = todo_tracker.read_todos()
    # Assert
    assert created_todo == expected_todo
    assert todos == [expected_todo]
    assert len(todos) == 1
