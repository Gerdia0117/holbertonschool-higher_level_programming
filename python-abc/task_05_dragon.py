#!/usr/bin/env python3
"""Module demonstrating mixins with SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin class that provides swimming capability."""

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability."""

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying from mixins."""

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")
