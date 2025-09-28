#!/usr/bin/env python3
"""Module for VerboseList class that extends list with notifications."""


class VerboseList(list):
    """A list class that prints notifications for modifications."""

    def append(self, item):
        """Add an item to the end of the list with notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable with notification."""
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """Remove the first occurrence of an item with notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at index with notification."""
        item = self[index]  # Get the item before popping
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
