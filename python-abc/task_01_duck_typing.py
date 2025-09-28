#!/usr/bin/env python3
"""Module for abstract Shape, Circle, Rectangle, and duck typing example."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of a shape (duck typing)."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
