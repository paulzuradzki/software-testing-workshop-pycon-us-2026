"""Demo: the same tests run under both unittest and pytest.

This file shows tests written in BOTH unittest and pytest styles.
No code to write here. Run the file with each runner and observe the
difference in what gets discovered.

How to run (from this module's directory):

    cd modules/1.2_unittest_and_pytest

    # unittest:
    uv run python -m unittest convert_f_to_c_START.py

    # pytest:
    uv run pytest convert_f_to_c_START.py -v

    # If you've activated .venv per the README setup, drop the `uv run` prefix.

Expected output:
- unittest reports 1 test (it only discovers the TestCase class).
- pytest reports 2 tests (it discovers the function AND the class).

Reflection questions:
- Why does pytest find 2 tests but unittest only 1?
- Which would you rather write going forward, and why?

Key takeaway: pytest is the workshop default. unittest is shown for awareness
since you may encounter it in legacy code; you do not need to master it.
"""

from unittest import TestCase


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


# NOTE: in practice it's better to limit the number of assertions in a single
# test so you can quickly identify which case failed. We'll cover how to cover
# many similar cases cleanly in Exercise 2.3 (parameterized tests).


# ---------- pytest style ----------------------------------------------------
# Plain module-level function. pytest discovers it because the function name
# starts with `test_`. unittest's runner ignores it because it's not a method
# on a TestCase class.


def test_convert_fahrenheit_to_celsius():
    assert convert_fahrenheit_to_celsius(212) == 100.0
    assert convert_fahrenheit_to_celsius(32) == 0.0
    assert convert_fahrenheit_to_celsius(-40) == -40.0
    assert convert_fahrenheit_to_celsius(100) == 37.77777777777778
    assert convert_fahrenheit_to_celsius(0) == -17.77777777777778


# ---------- unittest style --------------------------------------------------
# TestCase subclass with a test method. Both runners discover it. unittest
# requires the class boilerplate; pytest accepts the same shape for free.


class TestConvertFahrenheitToCelsius(TestCase):
    def test_convert_fahrenheit_to_celsius(self):
        self.assertEqual(convert_fahrenheit_to_celsius(212), 100.0)
        self.assertEqual(convert_fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(convert_fahrenheit_to_celsius(-40), -40.0)
        self.assertEqual(convert_fahrenheit_to_celsius(100), 37.77777777777778)
        self.assertEqual(convert_fahrenheit_to_celsius(0), -17.77777777777778)
