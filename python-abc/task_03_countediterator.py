#!/usr/bin/env python3
"""An iterator that keeps count of items yielded."""

class CountedIterator:
    """Iterator wrapper that counts how many items have been produced."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0.

        Args:
            iterable: An object to create an iterator from
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Get the next item, incrementing counter.

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: When no more items are available
        """
        item = next(self.iterator)  # May raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far.

        Returns:
            int: The count of items yielded
        """
        return self.counter

    def __iter__(self):
        """Return self to allow use in for loops."""
        return self
