#!/usr/bin/python3
"""
4-print_square.py
Module: provides a function to print a square with the character '#'.
"""


def print_square(size):
    """
    Print a square of size `size` using the character '#'.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
