"""Solution for Exercise 1.2: unittest style.

Run from the repo root with either runner:

    python -m unittest discover -s solutions/1.2_unittest_and_pytest -p 'test_unittest_style.py'
    pytest solutions/1.2_unittest_and_pytest/test_unittest_style.py -v

unittest only discovers `TestCase` subclasses. Module-level `test_*`
functions are invisible to it, which is the contrast Exercise 1.2
demonstrates. (We use `unittest discover` here because `python -m
unittest <path>` rejects directory names that start with a digit.)
"""

from unittest import TestCase


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


class TestConvertFahrenheitToCelsius(TestCase):
    def test_boiling_point(self):
        self.assertEqual(convert_fahrenheit_to_celsius(212), 100.0)

    def test_freezing_point(self):
        self.assertEqual(convert_fahrenheit_to_celsius(32), 0.0)

    def test_negative_forty_is_symmetric(self):
        self.assertEqual(convert_fahrenheit_to_celsius(-40), -40.0)
