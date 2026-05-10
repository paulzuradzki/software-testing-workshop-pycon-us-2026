"""Demo: parameterized tests (instructor walkthrough).

Worked example for Exercise 2.3. Same shape as the starter (multiple
inline assertions becoming one parameterized test), but exercising the
inverse function (Celsius to Fahrenheit) so the starter's table stays
empty for students to fill in.

Each tuple in the parametrize list becomes its own test ID in pytest's
verbose output. Failures isolate to the specific case rather than
short-circuiting on the first failed assert.

Run:

    cd modules/2.3_parameterized_tests
    pytest test_convert_c_to_f_DEMO.py -v
"""
import pytest


def convert_celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32


@pytest.mark.parametrize(
    "celsius,expected_fahrenheit",
    [
        (100, 212.0),
        (0, 32.0),
        (-40, -40.0),
        (37, 98.6),
        (-17.77777777777778, 0.0),
    ],
)
def test_convert_celsius_to_fahrenheit(celsius, expected_fahrenheit):
    assert convert_celsius_to_fahrenheit(celsius) == pytest.approx(expected_fahrenheit)
