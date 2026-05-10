"""Solution for Exercise 1.1.

Run with: pytest solutions/1.1_warm_up_temp_script/test_convert_f_to_c_warmup.py
Or as a script: python solutions/1.1_warm_up_temp_script/test_convert_f_to_c_warmup.py
"""


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def test_convert_fahrenheit_to_celsius():
    expected = round(26.6)
    result = round(convert_fahrenheit_to_celsius(80))
    assert result == expected, f"Received: {result}. Expected: {expected}."


if __name__ == "__main__":
    print(test_convert_fahrenheit_to_celsius())
