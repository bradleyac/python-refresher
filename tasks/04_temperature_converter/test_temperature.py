from temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
)


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0


def test_fahrenheit_to_celsius_boiling():
    assert fahrenheit_to_celsius(212) == 100.0


def test_fahrenheit_to_celsius_negative():
    assert fahrenheit_to_celsius(-40) == -40.0


def test_celsius_to_kelvin_absolute_zero():
    assert celsius_to_kelvin(-273.15) == 0.0


def test_rounding():
    assert celsius_to_fahrenheit(37) == 98.6


if __name__ == "__main__":
    test_freezing_point()
    test_boiling_point()
    test_fahrenheit_to_celsius_boiling()
    test_fahrenheit_to_celsius_negative()
    test_celsius_to_kelvin_absolute_zero()
    test_rounding()
    print("ok")
