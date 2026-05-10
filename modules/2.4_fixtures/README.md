# Exercise 2.4: Fixtures and tmp_path (25 min)

Goal: use pytest fixtures (built-in `tmp_path` and your own) to
write tests that touch real files, then compare with unittest's
`setUp`/`tearDown`. The SQLite demo shows the same pattern applied
to an in-memory database.

## Order to read

1. `todo.py`. File-based variant of the ToDoTracker that reads and
   writes JSON to disk.
2. `test_file_todo_DEMO.py`. pytest version using `tmp_path`. The
   instructor walks through this first.
3. `test_file_todo_unittest_DEMO.py`. The same test in unittest
   form with `setUp`/`tearDown`. Compare ergonomics.
4. `test_todo_fixture_DEMO.py`. A hand-rolled fixture using
   `@pytest.fixture`.

The hands-on starter for this exercise is being authored. For now,
follow along with the demos and try modifying them in place.

## Run the demos

```
cd modules/2.4_fixtures
pytest -v
```

## If you finish early (side quests)

- **Flakiness, improper cleanup:**
  `modules/side_quests/flakiness_cleanup/`. Two tests share a file in
  the cwd; passes alone, fails together. Identify and fix.
- **Flakiness, race condition:**
  `modules/side_quests/flakiness_race/`. Non-thread-safe counter under
  concurrent access. Identify and fix.
- Convert the unittest-style `setUp`/`tearDown` test in
  `test_file_todo_unittest_DEMO.py` into a pytest fixture. Compare
  readability.
