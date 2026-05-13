# Exercise 3.1: Dependency Injection

Hands-on for Part 3.

`ETL` takes a `reader` and a `writer` injected at construction time.
The `Reader` / `Writer` types are abstract base classes (`abc.ABC`)
defined in `storage.py`, along with concrete classes for S3, Postgres,
the local filesystem, and SQLite. Tests substitute fakes (or in-memory
SQLite) for the real network/database I/O.

```
pytest modules/3.1_dependency_injection -q
```

Files:

- `storage.py` (read-only). `Reader`/`Writer` ABCs and concrete
  subclasses: `LocalFileReader`, `LocalFileWriter`, `SqliteWriter`,
  `S3Reader` (lazy-imports `boto3`), `PostgresWriter` (lazy-imports
  `sqlalchemy`).
- `etl.py` (read-only). `ETL(reader, writer)` typed against the
  ABCs.
- `test_etl_START.py` (your worksheet). `FakeReader` plus three tests
  already wired up: `test_extract_with_fake`,
  `test_extract_with_local_file` (uses `LocalFileReader` + `tmp_path`),
  and `test_transform`. You write `FakeWriter` and `test_load`. Bonus:
  `test_run`.

For `test_load` you can pick either approach:

- **(A)** Recording fake. `FakeWriter` builds up a list of
  `(key, rows)` calls.
- **(B)** Real-ish. `SqliteWriter` from `storage.py` with
  `sqlite3.connect(":memory:")`. Lets you assert on actual queryable
  state.

Both demonstrate the substitution pattern. Either is right.

> Heads-up: substituting fakes / in-memory I/O is one strategy. It is
> not a replacement for an integration test against a real local
> Postgres. Both have a place. Today we're going deep on substitution.

Pointer to the deeper write-up (after the workshop):
[paulzuradzki.com: Dependency injection for Pythonistas](https://paulzuradzki.com/2025/7/dependency-injection-for-pythonistas/).
