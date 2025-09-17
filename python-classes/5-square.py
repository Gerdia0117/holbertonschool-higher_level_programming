#!/usr/bin/python3
"""Defines a class Square with size validation,
area calculation, and printing capability.
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square
        Args:
            size (int): size of the square
        """
        self.size = size  # use setter to validate

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation
        Args:
            value (int): new size value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'
        If size == 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
