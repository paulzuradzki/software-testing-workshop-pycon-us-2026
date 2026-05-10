"""Solution for Exercise 3.1: DI tests with fakes and SQLite."""
from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

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
    def __init__(self, rows_by_name):
        self.rows_by_name = rows_by_name
        self.reads = []

    def read(self, name):
        self.reads.append(name)
        return self.rows_by_name[name]


class FakeWriter:
    def __init__(self):
        self.writes = []

    def write(self, key, rows):
        self.writes.append((key, rows))


def test_extract_with_fake():
    reader = FakeReader({"users": SOURCE_ROWS})
    etl = ETL(reader=reader, writer=None)

    rows = etl.extract("users")

    assert rows == SOURCE_ROWS
    assert reader.reads == ["users"]


def test_extract_with_local_file(tmp_path: Path):
    csv_path = tmp_path / "users.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "name", "email"])
        w.writeheader()
        w.writerows(SOURCE_ROWS)

    reader = LocalFileReader(base_path=tmp_path)
    etl = ETL(reader=reader, writer=None)

    assert etl.extract("users.csv") == SOURCE_ROWS


def test_transform():
    etl = ETL(reader=None, writer=None)

    assert etl.transform(SOURCE_ROWS) == EXPECTED_ROWS


def test_load_with_fake_writer():
    writer = FakeWriter()
    etl = ETL(reader=None, writer=writer)

    etl.load(EXPECTED_ROWS, "users_transformed")

    assert writer.writes == [("users_transformed", EXPECTED_ROWS)]


def test_load_with_sqlite_writer():
    conn = sqlite3.connect(":memory:")
    writer = SqliteWriter(conn)
    etl = ETL(reader=None, writer=writer)

    etl.load(EXPECTED_ROWS, "users_transformed")

    persisted = list(conn.execute(
        "SELECT id, name_redacted, email_redacted FROM users_transformed ORDER BY id"
    ))
    assert persisted == [
        ("1", "A***e", "a***************m"),
        ("2", "B*b",   "b*************m"),
    ]


def test_run():
    reader = FakeReader({"users": SOURCE_ROWS})
    writer = FakeWriter()
    etl = ETL(reader=reader, writer=writer)

    out = etl.run("users", "users_transformed")

    assert out == EXPECTED_ROWS
    assert writer.writes == [("users_transformed", EXPECTED_ROWS)]
