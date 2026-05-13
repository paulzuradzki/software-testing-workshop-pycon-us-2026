from converter.convert_temp import convert_fahrenheit_to_celsius


def test_convert_fahrenheit_to_celsius():
    assert convert_fahrenheit_to_celsius(212) == 100.0
    assert convert_fahrenheit_to_celsius(32) == 0.0
    assert convert_fahrenheit_to_celsius(-40) == -40.0
    assert convert_fahrenheit_to_celsius(100) == 37.77777777777778
    assert convert_fahrenheit_to_celsius(0) == -17.77777777777778
    assert convert_fahrenheit_to_celsius(-40) == -40.0
