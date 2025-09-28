#!/usr/bin/env python3
"""Module for CountedIterator class that tracks iteration count."""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator and counter.

        Args:
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the current count of items that have been iterated.

        Returns:
            int: The number of items iterated over so far.
        """
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def __iter__(self):
        """Return the iterator object itself."""
        return self
