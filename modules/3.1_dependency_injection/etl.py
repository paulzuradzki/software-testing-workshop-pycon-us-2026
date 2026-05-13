"""ETL pipeline (DI version).

Read rows from a source, mask sensitive fields, write the rows to a
target. The reader and writer are injected. In production they wrap
S3 and Postgres. In tests they're fakes or in-memory SQLite.

The reader/writer types are abstract base classes defined in
storage.py: an explicit contract that concrete classes inherit from.
"""

from __future__ import annotations

from pathlib import Path
from pprint import pprint

from storage import LocalFileReader, LocalFileWriter, Reader, Writer


def main():
    here = Path(__file__).parent
    reader = LocalFileReader(here)
    writer = LocalFileWriter(here)

    print("Input user data:")
    pprint(reader.read("input.csv"), sort_dicts=False)

    etl = ETL(reader, writer)
    etl.run(source_key="input.csv", target_key="output.csv")

    print("\nOutput with redacted PII:")
    print((here / "output.csv").read_text())


def _mask(s: str) -> str:
    return s[0] + "*" * (len(s) - 2) + s[-1]


class ETL:
    def __init__(self, reader: Reader, writer: Writer):
        self.reader = reader
        self.writer = writer

    def extract(self, source_key: str) -> list[dict]:
        return self.reader.read(source_key)

    def transform(self, rows: list[dict]) -> list[dict]:
        return [
            {
                "id": r["id"],
                "name_redacted": _mask(r["name"]),
                "email_redacted": _mask(r["email"]),
            }
            for r in rows
        ]

    def load(self, rows: list[dict], target_key: str) -> None:
        self.writer.write(target_key, rows)

    def run(self, source_key: str, target_key: str) -> list[dict]:
        rows = self.extract(source_key)
        out = self.transform(rows)
        self.load(out, target_key)
        return out


if __name__ == "__main__":
    main()
