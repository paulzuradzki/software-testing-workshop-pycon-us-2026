"""
Before we introduce pytest and unittest,
let's familiarize with basic asserts.
"""


def convert_celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32


def test_convert_celsius_to_fahrenheit():
    assert convert_celsius_to_fahrenheit(100) == 212.0
    assert convert_celsius_to_fahrenheit(0) == 32.0
    assert convert_celsius_to_fahrenheit(-40) == -40.0
    assert convert_celsius_to_fahrenheit(100) == 212.0
    assert convert_celsius_to_fahrenheit(0) == 32.0
    assert convert_celsius_to_fahrenheit(-40) == -40.0


if __name__ == "__main__":
    # manual test
    print(convert_celsius_to_fahrenheit(100))  # 212.0

    # test function invocation
    test_convert_celsius_to_fahrenheit()
