"""Side quest: flakiness from improper cleanup (~10-15 min).

Two tests below both touch a file named "scratch.txt" in the current
working directory. Run them and observe:

    uv run pytest modules/side_quests/flakiness_cleanup -v
    uv run pytest modules/side_quests/flakiness_cleanup -v -k writes
    uv run pytest modules/side_quests/flakiness_cleanup -v -k missing

One test passes in isolation and fails when run with the other. The
task: identify which test leaks state, explain the order dependency,
and fix both tests so they pass together and apart, in any order.

Hints if needed. Look up pytest's tmp_path fixture. Look up fixtures
that yield and run teardown after the yield. Either approach works.
Do not solve it by adding a sleep or by hard-coding a test order.
"""

from pathlib import Path

SCRATCH = Path("scratch.txt")


def test_writes_scratch_file():
    # Write some content and check it landed.
    SCRATCH.write_text("hello")
    assert SCRATCH.read_text() == "hello"


def test_scratch_file_is_missing():
    # A fresh checkout of the repo has no scratch.txt next to this test.
    assert not SCRATCH.exists()
