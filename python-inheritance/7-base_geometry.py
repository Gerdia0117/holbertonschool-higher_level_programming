#!/usr/bin/python3
"""Defines a BaseGeometry class with area and validation methods."""

class BaseGeometry:
    """A base geometry class with validation functionality."""

    def area(self):
        """Raise an Exception indicating area() is not implemented.

        Raises:
            Exception: Always with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
