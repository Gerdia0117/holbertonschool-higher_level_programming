#!/usr/bin/python3
"""Defines BaseGeometry class with area method."""


class BaseGeometry:
    """Base geometry class with uniplemented area method."""

    def area(self):
        """Raise Exception that area is not implemented.

        Raises:
        Exceptiom: Always with messafe 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
