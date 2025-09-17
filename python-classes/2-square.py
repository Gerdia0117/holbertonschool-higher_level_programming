#!/usr/bin/python3
"""Defines a class Square with size validation"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
