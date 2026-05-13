"""Concrete reader/writer implementations for the ETL pipeline.

The contract is captured by the `Reader` and `Writer` abstract base
classes below (`abc.ABC` + `@abstractmethod`). ETL only sees those
ABCs; the concrete class plugs in at the seam.

Why ABC and not `typing.Protocol` here:

- `@abstractmethod` is enforced at *instantiation*. `LocalFileReader()`
  raises `TypeError` if a subclass forgets `read`. That makes the
  contract obvious to a reader of the file.
- pyright/mypy will flag a missing method on a subclass at the
  subclass definition, not just at the call site.
- Protocol gives you structural (duck) typing and is also valid.
  Pythonic taste varies. We pick ABC here because the explicit
  contract is easier to teach.

Pick the implementation that fits the context:

- Production:   `S3Reader` + `PostgresWriter`
- Local dev:    `LocalFileReader` + `LocalFileWriter`
- Testing:      `FakeReader` / `FakeWriter` (defined per-test) or
                `SqliteWriter` against an in-memory SQLite connection

Test fakes in `test_etl_START.py` don't inherit from `Reader` /
`Writer`. Duck typing still works at the call site because ETL never
calls `isinstance`. Inheriting is a stricter style; both are valid.

`S3Reader` and `PostgresWriter` lazy-import `boto3` / `sqlalchemy`
inside `__init__`, so this module imports cleanly without those
packages installed. They're here as concrete examples; the workshop
exercises don't instantiate them.
"""

from __future__ import annotations

import csv
import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class Reader(ABC):
    """Contract: `read(key) -> list[dict]`."""

    @abstractmethod
    def read(self, key: str) -> list[dict]: ...


class Writer(ABC):
    """Contract: `write(key, rows) -> None`."""

    @abstractmethod
    def write(self, key: str, rows: list[dict]) -> None: ...


# --- Local filesystem implementations ---------------------------------------


class LocalFileReader(Reader):
    """Reads CSV from `<base_path>/<key>`."""

    def __init__(self, base_path: str | Path):
        self.base_path = Path(base_path)

    def read(self, key: str) -> list[dict]:
        with (self.base_path / key).open() as f:
            return list(csv.DictReader(f))


class LocalFileWriter(Writer):
    """Writes rows as CSV to `<base_path>/<key>`."""

    def __init__(self, base_path: str | Path):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def write(self, key: str, rows: list[dict]) -> None:
        path = self.base_path / key
        if not rows:
            path.write_text("")
            return
        with path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)


# --- SQLite (in-process database) -------------------------------------------


class SqliteWriter(Writer):
    """Writes rows to a SQLite table named `key`. Use
    `sqlite3.connect(":memory:")` for fast, isolated tests.

    Workshop-grade: uses string interpolation for table/column names.
    Don't accept untrusted input for `key` or row keys in real code.
    """

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def write(self, key: str, rows: list[dict]) -> None:
        if not rows:
            return
        cols = list(rows[0].keys())
        col_decls = ", ".join(f"{c} TEXT" for c in cols)
        placeholders = ", ".join("?" for _ in cols)
        self.conn.execute(f'CREATE TABLE IF NOT EXISTS "{key}" ({col_decls})')
        self.conn.executemany(
            f'INSERT INTO "{key}" ({", ".join(cols)}) VALUES ({placeholders})',
            [tuple(str(r[c]) for c in cols) for r in rows],
        )
        self.conn.commit()


# --- Cloud / production implementations (lazy-imported) ---------------------


class S3Reader(Reader):
    """Reads CSV from `s3://<bucket>/<key>`. Requires `boto3`."""

    def __init__(self, bucket: str, client=None):
        if client is None:
            import boto3  # lazy import keeps storage.py importable without boto3

            client = boto3.client("s3")
        self.bucket = bucket
        self.client = client

    def read(self, key: str) -> list[dict]:
        response = self.client.get_object(Bucket=self.bucket, Key=key)
        body = response["Body"].read().decode("utf-8")
        return list(csv.DictReader(body.splitlines()))


class PostgresWriter(Writer):
    """Writes rows to a Postgres table. Requires `sqlalchemy`."""

    def __init__(self, db_url: str):
        from sqlalchemy import create_engine  # lazy import

        self.engine = create_engine(db_url)

    def write(self, key: str, rows: list[dict]) -> None:
        from sqlalchemy import text

        if not rows:
            return
        cols = list(rows[0].keys())
        placeholders = ", ".join(":" + c for c in cols)
        with self.engine.begin() as conn:
            conn.execute(
                text(f"INSERT INTO {key} ({', '.join(cols)}) VALUES ({placeholders})"),
                rows,
            )
