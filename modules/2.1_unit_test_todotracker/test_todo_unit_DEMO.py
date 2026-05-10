"""Demo: unit tests for ToDoTracker (instructor walkthrough).

Worked example for Exercise 2.1. Each test exercises a single method on a
fresh tracker, using AAA. Fixtures arrive in 2.4.

Compare with 2.2 (integration): create and read never chain inside a
single test here. Each test pins down the behavior of a single method.

Run:

    cd modules/2.1_unit_test_todotracker
    pytest test_todo_unit_DEMO.py -v
"""
from todo import ToDoTracker, ToDo


def test_create_todo_returns_the_stored_value():
    # Arrange
    tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)

    # Act
    created_todo = tracker.create_todo(expected_todo)

    # Assert
    assert created_todo == expected_todo
    assert len(tracker.todos) == 1


def test_search_todos_finds_a_match_by_description():
    # Arrange
    tracker = ToDoTracker()
    expected_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    tracker.create_todo(expected_todo)

    # Act
    matches = tracker.search_todos("groceries")

    # Assert
    assert matches == [expected_todo]
