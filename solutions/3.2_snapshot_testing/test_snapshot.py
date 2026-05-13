"""Solution for Exercise 3.2: captured snapshot baseline."""

import pytest
from gnarly import compute_invoice

CASES = [
    ("regular_small", (1, 10.0, "regular", None)),
    ("silver_taxexempt", (1, 10.0, "silver", None)),
    ("gold_midsize", (5, 20.0, "gold", None)),
    ("platinum_bulk_coupon", (25, 5.0, "platinum", "NEW10")),
    ("regular_coupon", (3, 30.0, "regular", "NEW10")),
]

EXPECTED = {
    "regular_small": 10.89,
    "silver_taxexempt": 9.5,
    "gold_midsize": 97.99,
    "platinum_bulk_coupon": 97.99,
    "regular_coupon": 88.19,
}


@pytest.mark.parametrize("name,args", CASES, ids=[c[0] for c in CASES])
def test_invoice_snapshot(name, args):
    assert compute_invoice(*args) == EXPECTED[name]
