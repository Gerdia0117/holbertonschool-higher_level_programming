#!/usr/bin/python3
"""
This module defines a function to print a square with '#' characters.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size of the square (length of sides)

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(2)
        ##
        ##
        >>> print_square(0)

        >>> print_square(1)
        #
        >>> try:
        ...     print_square(-1)
        ... except Exception as e:
        ...     print(e)
        size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
