#!/usr/bin/python3
"""Defines a class Square with size, position,
area calculation, and printing capability.
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square
        Args:
            size (int): size of the square
            position (tuple): 2-tuple of positive integers
        """
        self.size = size        # validate via setter
        self.position = position  # validate via setter

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation
        Args:
            value (tuple): must be a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'
        Uses position for indentation.
        """
        if self.__size == 0:
            print()
            return

        # Print newlines for vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each line with spaces for horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
