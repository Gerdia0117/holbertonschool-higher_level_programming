#!/usr/bin/python3
"""Define a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with additional functionality."""

    def print_sorted(self):
        """print the list in acending sorted order."""
        print(sorted(self))
