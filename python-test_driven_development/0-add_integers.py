#!/usr/bin/python3
"""
Module provides a function to add two integers.

add_integer function takes two arguments and returns their sum
If either argument is not an integer or float, a TypeError is raised
"""


def add_integer(a, b=98):
    """Return the sum of two integers a and b.

    Arguments:
    a -- the first number (int or float)
    b -- the second number (int or float), defaults to 98

    Raises:
    TypeError -- if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
