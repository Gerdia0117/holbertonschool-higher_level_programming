#!/usr/bin/python3
"""Defines a BaseGeometry class with validation methods."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an Exception indicating area() is not implemented.

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as a positive integer.

        Args:
            name (str): Name of the parameter
            value (int): Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
