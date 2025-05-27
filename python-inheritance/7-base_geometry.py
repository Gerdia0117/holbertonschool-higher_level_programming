#!/usr/bin/python3
"""Defines a BaseGeometry class with validation methods."""


class BaseGeometry:
    """Base class for geometry operations with input validation."""

    def area(self):
        """Raises an Exception indicating area() is not implemented.

        Raises:
            Exception: 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is a positive integer.

        Args:
            name (str): Name of the parameter (used in error messages).
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value ≤ 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
