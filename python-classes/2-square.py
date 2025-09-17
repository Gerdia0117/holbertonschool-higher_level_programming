#!/usr/bin/pythong3
"""Define a class square with size validation"""


class Square:
    """Class that define a square """

    def __init__(self, side=0):
        """Initialize a new square
        Args:
            size (init): size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size