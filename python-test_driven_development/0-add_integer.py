#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function handles type checking and conversion from floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers after proper type checking and conversion.

    Args:
        a: First number (integer or float)
        b: Second number (integer or float, defaults to 98)

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If either a or b is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    # Handle NaN (Not a Number) float values
    if isinstance(a, float) and a != a:  # check for NaN
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:  # check for NaN
        raise ValueError("cannot convert float NaN to integer")
    try:
        return int(a) + int(b)
    except (OverflowError, ValueError) as e:
        raise e
