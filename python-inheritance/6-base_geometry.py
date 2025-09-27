#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raises an exception when area() is not implemented."""
        raise Exception("area() is not implemented")
