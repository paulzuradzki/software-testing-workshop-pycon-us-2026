"""Exercise 3.2: Snapshot test for compute_invoice.

`compute_invoice` is intentionally opaque. Snapshot pattern:

  1. Pick interesting inputs.
  2. Run the function. Capture the outputs.
  3. Lock those outputs in as the baseline.
  4. Any future change that drifts the output fails the test loudly.

Workflow for this exercise:

  1. Run this file as a script. It prints the current outputs:

         python modules/3.2_snapshot_testing/test_snapshot_START.py

  2. Paste the printed lines into the EXPECTED dict below.
  3. Run the tests:

         pytest modules/3.2_snapshot_testing -q

  4. Modify gnarly.py: bump the tax rate, change a threshold.
     Watch the tests fail loudly. That is the safety net.

Pointer: a production-grade snapshot library is `approvaltests` on
PyPI. The hand-rolled version here keeps the moving parts visible.
The mechanism is `assert actual == captured_baseline`.
"""
import pytest

from gnarly import compute_invoice


CASES = [
    ("regular_small",        (1,  10.0, "regular",  None)),
    ("silver_taxexempt",     (1,  10.0, "silver",   None)),
    ("gold_midsize",         (5,  20.0, "gold",     None)),
    ("platinum_bulk_coupon", (25,  5.0, "platinum", "NEW10")),
    ("regular_coupon",       (3,  30.0, "regular",  "NEW10")),
]

# TODO: populate by running this file as a script (see module docstring).
EXPECTED = {
    # "regular_small": ...,
}


@pytest.mark.parametrize("name,args", CASES, ids=[c[0] for c in CASES])
def test_invoice_snapshot(name, args):
    assert name in EXPECTED, f"snapshot for {name!r} not captured yet"
    assert compute_invoice(*args) == EXPECTED[name]


if __name__ == "__main__":
    print("Paste these into EXPECTED:\n")
    for name, args in CASES:
        result = compute_invoice(*args)
        print(f'    "{name}": {result!r},')
