#!/usr/bin/env python3
"""Module for Shape abstract class, Circle, Rectangle, and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

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
    """Print area and perimeter of a given shape (duck typing)."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
