#!/usr/bin/python3
"""
This module defines a function add_integer.
It adds two integers or floats after casting them to integers.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
