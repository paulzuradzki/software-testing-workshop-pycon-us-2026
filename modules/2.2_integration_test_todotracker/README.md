# Exercise 2.2: Integration test ToDoTracker (10 min)

Goal: write a single test that exercises more than one method
together (create + read), verifying the methods cooperate. Compare
this with 2.1, where each test pinned down a single method in
isolation.

## Order to read

1. `todo.py`. Same class as Exercise 2.1.
2. `test_todo_integration_DEMO.py`. The instructor walks through this
   first. One worked integration test plus a note on what it catches
   that 2.1's unit tests would miss.
3. `test_todo_integration_START.py`. Your work.

## What does this catch that the unit tests don't?

The demo seeds an open todo *and* a completed todo, then asserts
`read_todos()` returns both. If a future refactor silently filters
completed items out of `read_todos`, this test fails immediately. The
2.1 unit tests keep passing because they exercise `create_todo` and
`search_todos` in isolation and never read back over a mixed list.

Rule of thumb: when two methods are supposed to compose, write at
least one test that composes them.

## Run

```
cd modules/2.2_integration_test_todotracker
pytest test_todo_integration_START.py -v
```

## If you finish early (side quests)

- Write an integration test that creates 3 todos and verifies
  `search_todos("buy")` returns the right subset.
- Write an integration test that creates, then deletes, then
  re-reads. Decide what state the tracker should be in.
- Compare your unit tests (2.1) with this integration test. Pick
  which one would catch a `create_todo` bug faster.
