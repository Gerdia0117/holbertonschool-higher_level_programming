#!/usr/bin/env python3
"""Defines an abstract Animal class and concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that should be implemented by subclasses.

        Returns:
            str: The sound the animal makes.
        """
        pass


class Dog(Animal):
    """Concrete class representing a Dog."""

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            str: 'Bark'
        """
        return "Bark"


class Cat(Animal):
    """Concrete class representing a Cat."""

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            str: 'Meow'
        """
        return "Meow"
