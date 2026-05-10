"""Exercise 3.1: Test ETL with injected fakes.

`ETL` takes a `reader` and a `writer`. Production plugs in `S3Reader`
plus `PostgresWriter`. Tests plug in something cheaper.

What's already wired up:

- `test_extract_with_fake`: uses an in-memory `FakeReader`. The key is
  a logical name; no filesystem touched.
- `test_extract_with_local_file`: uses the real `LocalFileReader`
  against a CSV file in pytest's `tmp_path`. Same `extract` contract,
  exercised through real file I/O.
- `test_transform`: pure function; no fakes needed.

Remaining work:

- Pick a writer strategy for `test_load`. Either is fine:

    Option A: `FakeWriter` (recording fake). Builds up a list of
    `(key, rows)` calls. Cleanest for asserting the wiring.

    Option B: `SqliteWriter` from storage.py with
    `sqlite3.connect(":memory:")`. Closer to a real database; allows
    assertions against actual queryable state.

- Bonus: `test_run` wires both pieces through `ETL.run`.

Heads-up: substituting fakes and in-memory I/O is one strategy. It
does not replace an integration test against a real local Postgres.
Both have a place. Today the focus is substitution.

Run from the repo root:

    pytest modules/3.1_dependency_injection -q
"""
from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

import pytest

from etl import ETL
from storage import LocalFileReader, SqliteWriter


SOURCE_ROWS = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob",   "email": "bob@example.com"},
]

EXPECTED_ROWS = [
    {"id": "1", "name_redacted": "A***e", "email_redacted": "a***************m"},
    {"id": "2", "name_redacted": "B*b",   "email_redacted": "b*************m"},
]


class FakeReader:
    """In-memory stand-in. Maps a logical name to canned rows."""

    def __init__(self, rows_by_name):
        self.rows_by_name = rows_by_name
        self.reads = []

    def read(self, name):
        self.reads.append(name)
        return self.rows_by_name[name]


def test_extract_with_fake():
    # Arrange: logical key, no filesystem
    reader = FakeReader({"users": SOURCE_ROWS})
    etl = ETL(reader=reader, writer=None)

    # Act
    rows = etl.extract("users")

    # Assert
    assert rows == SOURCE_ROWS
    assert reader.reads == ["users"]


def test_extract_with_local_file(tmp_path: Path):
    # Arrange: write a real CSV into tmp_path; key IS the filename here
    csv_path = tmp_path / "users.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "name", "email"])
        w.writeheader()
        w.writerows(SOURCE_ROWS)

    reader = LocalFileReader(base_path=tmp_path)
    etl = ETL(reader=reader, writer=None)

    # Act
    rows = etl.extract("users.csv")

    # Assert
    assert rows == SOURCE_ROWS


def test_transform():
    # Arrange
    etl = ETL(reader=None, writer=None)

    # Act
    rows = etl.transform(SOURCE_ROWS)

    # Assert
    assert rows == EXPECTED_ROWS


# Pick one (or do both!): a recording fake OR in-memory SQLite.

class FakeWriter:
    """Recording fake. Real writers persist somewhere; this one just
    remembers what it was asked to write so the test can inspect.
    """
    # TODO: implement __init__ to set up storage for recorded writes.
    # TODO: implement write(self, key, rows) to record the call.


def test_load():
    # TODO: Option A. Build a FakeWriter and an ETL using it; OR
    # TODO: Option B. Build a SqliteWriter on sqlite3.connect(":memory:")
    #                 and an ETL using it.
    # TODO: call etl.load(EXPECTED_ROWS, "users_transformed").
    # TODO: assert the writer received the right key + rows.
    raise AssertionError("TODO: complete test_load with the writer of your choice")


# Bonus, optional:
@pytest.mark.skip(reason="bonus: remove the skip once you tackle it")
def test_run():
    # TODO: wire FakeReader + your writer through ETL.
    # TODO: call etl.run("users", "users_transformed").
    # TODO: assert the writer received the transformed rows.
    raise AssertionError("TODO: bonus: wire run() end-to-end")
