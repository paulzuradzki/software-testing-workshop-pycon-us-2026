"""Side quest: flakiness from a race condition (~10-15 min).

Optional puzzle for fast finishers. The `Counter` class below is not
thread-safe. The test spawns many threads that each increment the counter
in a tight loop and asserts on the final total.

Steps:
1. Run the test several times. Expect intermittent failures. That
   intermittent failure is the point of the exercise.
2. Identify the race condition in `Counter.increment`.
3. Fix it. Two reasonable options: guard the mutation with a
   `threading.Lock`, or replace the shared counter with per-thread totals
   summed at the end.
4. Re-run the test 5-10 times to confirm the fix holds.

Run from the repo root:

    uv run pytest modules/side_quests/flakiness_race/ -v

Re-run with `--count=10` style loops via the shell, or press up-arrow
and Enter a few times. Running once is not enough to trust the result.
"""

import threading

import pytest

NUM_THREADS = 50
ITERATIONS_PER_THREAD = 2000
EXPECTED_TOTAL = NUM_THREADS * ITERATIONS_PER_THREAD


class Counter:
    """Shared counter. Not thread-safe."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        # Read-modify-write is not atomic across threads.
        current = self.value
        current += 1
        self.value = current


def _worker(counter: Counter, iterations: int) -> None:
    for _ in range(iterations):
        counter.increment()


def test_counter_final_value_matches_expected() -> None:
    """Spawn workers, increment in parallel, assert the total.

    The test is expected to fail some of the time until the race is
    fixed. A few runs in a row will surface the flakiness.
    """
    counter = Counter()
    threads = [
        threading.Thread(target=_worker, args=(counter, ITERATIONS_PER_THREAD))
        for _ in range(NUM_THREADS)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert counter.value == EXPECTED_TOTAL, (
        f"expected {EXPECTED_TOTAL}, got {counter.value} "
        f"(lost {EXPECTED_TOTAL - counter.value} increments to the race)"
    )
