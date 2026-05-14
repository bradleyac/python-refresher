"""Task 4: Temperature converter.

Implement three pure functions that convert between Celsius, Fahrenheit, and
Kelvin. Round each result to 2 decimal places before returning it.

Formulas:
    F = C * 9/5 + 32
    K = C + 273.15

Examples:
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> fahrenheit_to_celsius(212)
    100.0
    >>> celsius_to_kelvin(-273.15)
    0.0
"""


def celsius_to_fahrenheit(c: float) -> float:
    raise NotImplementedError


def fahrenheit_to_celsius(f: float) -> float:
    raise NotImplementedError


def celsius_to_kelvin(c: float) -> float:
    raise NotImplementedError


if __name__ == "__main__":
    c = float(input("Enter degrees Celsius: "))
    print(f"{c} C = {celsius_to_fahrenheit(c)} F")
    print(f"{c} C = {celsius_to_kelvin(c)} K")
