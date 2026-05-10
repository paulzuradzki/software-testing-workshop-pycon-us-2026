import pytest
from todo import ToDo, ToDoTracker


@pytest.fixture
def todo_tracker():
    return ToDoTracker()

def test_create_todo(todo_tracker):
    # Arrange
    todo = ToDo(
        id=1, title="Buy groceries", description="Buy groceries", completed=False
    )
    expected_todo = ToDo(
        id=1, title="Buy groceries", description="Buy groceries", completed=False
    )

    # Act
    created_todo = todo_tracker.create_todo(todo)

    # Assert
    assert created_todo == expected_todo
    assert len(todo_tracker.todos) == 1
    assert todo_tracker.todos[0] == expected_todo
