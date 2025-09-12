#!/usr/bin/python3
"""
0-add_integer.py
Module to perform the addition of 2 numbers, ensuring inputs are int or float,
casting floats to ints, and raising errors otherwise.
"""


def add_integer(a, b=98):
    """
    Add two integers after validating types and casting floats to ints.

    Args:
        a (int|float): The first number to add.
        b (int|float): The second number to add (defaults to 98).

    Returns:
        int: The sum of a and b, with any floats truncated to integers.

    Raises:
        TypeError: If a or b is not an int or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100.7, -2.3)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
