"""Solution for Exercise 2.3 (Parameterized tests)."""
import pytest


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


@pytest.mark.parametrize(
    "fahrenheit,expected_celsius",
    [
        (212, 100.0),
        (32, 0.0),
        (-40, -40.0),
        (100, 37.77777777777778),
        (0, -17.77777777777778),
    ],
)
def test_convert_fahrenheit_to_celsius(fahrenheit, expected_celsius):
    assert convert_fahrenheit_to_celsius(fahrenheit) == expected_celsius
