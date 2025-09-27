#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A custom list class that inherits from Python's built-in list."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
