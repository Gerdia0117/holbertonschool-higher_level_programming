#!/usr/bin/env python3
"""A list subclass that prints notifications for modifications."""

class VerboseList(list):
    """A list that prints notifications for modifications."""

    def append(self, item):
        """Add an item to the end of the list with notification.

        Args:
            item: The item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable with notification.

        Args:
            iterable: An iterable of items to add
        """
        length_before = len(self)
        super().extend(iterable)
        added = len(self) - length_before
        print(f"Extended the list with [{added}] items.")

    def remove(self, item):
        """Remove first occurrence of item with notification.

        Args:
            item: The item to remove

        Raises:
            ValueError: If item is not in list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index with notification.

        Args:
            index: Position of item to remove (default last)

        Returns:
            The popped item

        Raises:
            IndexError: If list is empty or index is out of range
        """
        item = self[index]  # Get item before popping for message
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
