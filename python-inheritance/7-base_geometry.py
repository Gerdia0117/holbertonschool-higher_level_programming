#!/usr/bin/python3
"""Defines BaseGeometry class with area and validation methods."""


class BaseGeometry:
    """Base geometry class with area and validation methods."""

    def area(self):
        """Raise Exception that area is not implemented.

        Raises:
            Exception: Always with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
