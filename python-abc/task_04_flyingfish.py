#!/usr/bin/env python3
"""Demonstration of multiple inheritance with Fish and Bird."""

class Fish:
    """Represents a fish."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A creature that inherits from both Fish and Bird."""

    def fly(self):
        """Override Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override both parents' habitat methods."""
        print("The flying fish lives both in water and the sky!")
