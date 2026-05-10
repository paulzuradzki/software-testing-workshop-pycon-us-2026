"""Solution for Exercise 1.2: pytest style.

Run from the repo root:

    pytest solutions/1.2_unittest_and_pytest/test_pytest_style.py -v

pytest discovers both `test_*` functions and `Test*` classes. The
idiomatic pytest form is a plain module-level function with `assert`.
"""


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def test_boiling_point():
    assert convert_fahrenheit_to_celsius(212) == 100.0


def test_freezing_point():
    assert convert_fahrenheit_to_celsius(32) == 0.0


def test_negative_forty_is_symmetric():
    assert convert_fahrenheit_to_celsius(-40) == -40.0
