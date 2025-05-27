#!/usr/bin/python3
"""Defines a BaseGeometry class with integer validation."""


class BaseGeometry:
    """A base class for geometry operations."""

    def area(self):
        """Raises an Exception indicating area() is not implemented.

        Raises:
            Exception: Always with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
