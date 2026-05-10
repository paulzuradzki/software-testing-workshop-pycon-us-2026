"""Exercise:

The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9

Update test_convert_fahrenheit_to_celsius to verify that the program is working correctly.

Run with:
    python convert_f_to_c_START.py
    # or, without activating .venv:
    uv run python convert_f_to_c_START.py
"""
def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

# FIXME: update this test to make input-output assertions
def test_convert_fahrenheit_to_celsius():
    raise NotImplementedError("Not implemented")

if __name__ == "__main__":
    test_convert_fahrenheit_to_celsius()
