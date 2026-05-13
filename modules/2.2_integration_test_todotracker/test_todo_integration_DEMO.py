"""Demo: integration test for ToDoTracker (instructor walkthrough).

Worked example for Exercise 2.2. One test, two methods cooperating
(`create_todo` + `read_todos`). Compare with 2.1, where each test
pinned down a single method in isolation.

Why bother when 2.1's unit tests already pass?

This test seeds the tracker with one open and one completed todo,
then asserts `read_todos()` returns both. If a future refactor changes
`read_todos` to silently filter out completed items (a plausible bug
or spec drift), this test fails immediately. The 2.1 unit tests keep
passing because they cover `create_todo` and `search_todos` in
isolation and never read back over a mixed list.

Rule of thumb: when two methods are supposed to compose, write at
least one test that composes them.

Run:

    cd modules/2.2_integration_test_todotracker
    pytest test_todo_integration_DEMO.py -v
"""

from todo import ToDo, ToDoTracker


def test_read_returns_both_open_and_completed_todos():
    # Arrange
    tracker = ToDoTracker()
    open_todo = ToDo(id=1, title="Buy groceries", description="Buy groceries", completed=False)
    done_todo = ToDo(id=2, title="Pay rent", description="Pay rent", completed=True)
    tracker.create_todo(open_todo)
    tracker.create_todo(done_todo)

    # Act
    todos = tracker.read_todos()

    # Assert
    assert todos == [open_todo, done_todo]
