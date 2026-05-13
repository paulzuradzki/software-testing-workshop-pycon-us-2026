"""Exercise 2.3: Parameterized Tests

Convert the individual assertions below into a single parameterized test
using @pytest.mark.parametrize.

Hint: the decorator takes two arguments:
  1. A string with comma-separated parameter names (e.g., "fahrenheit,expected_celsius")
  2. A list of tuples, one per test case

Run with:
    pytest test_convert_f_to_c_START.py -v
    # or, without activating .venv:
    uv run pytest test_convert_f_to_c_START.py -v
"""


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


# TODO: Replace the test below with a parameterized version.
#
# Cases to include in the parametrize table:
#   (212, 100.0)
#   (32, 0.0)
#   (-40, -40.0)
#   (100, 37.77777777777778)
#   (0, -17.77777777777778)


def test_convert_fahrenheit_to_celsius():
    assert convert_fahrenheit_to_celsius(212) == 100.0
    assert convert_fahrenheit_to_celsius(32) == 0.0
    assert convert_fahrenheit_to_celsius(-40) == -40.0
    assert convert_fahrenheit_to_celsius(100) == 37.77777777777778
    assert convert_fahrenheit_to_celsius(0) == -17.77777777777778
