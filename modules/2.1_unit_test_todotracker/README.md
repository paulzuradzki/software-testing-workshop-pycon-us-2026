# Exercise 2.1: Unit test ToDoTracker (10 min)

Goal: write isolated unit tests for individual methods of
`ToDoTracker`. Each test exercises a single method on a fresh
tracker.

## Order to read

1. `todo.py`. The class under test. Skim the `ToDoTracker` API:
   `create_todo`, `read_todos`, `search_todos`, `update_todo`,
   `delete_todo`.
2. `test_todo_unit_DEMO.py`. The instructor walks through this first.
   Two worked unit tests on a fresh tracker.
3. `test_todo_unit_START.py`. Your work. The Arrange step is already
   filled in for you. Complete the Act and Assert for each test.

## Run

```
cd modules/2.1_unit_test_todotracker
pytest test_todo_unit_START.py -v
```

## If you finish early (side quests)

- Write a test for `update_todo`. Pick the behavior you want for an
  out-of-range index.
- Write a test for `delete_todo`. Pick the behavior you want on an
  empty tracker.
- Write a test for `search_todos` with a query that matches nothing.
  Decide whether it should return `[]`, `None`, or raise.
