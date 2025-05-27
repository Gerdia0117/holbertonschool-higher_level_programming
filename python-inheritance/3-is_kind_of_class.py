#!/usr/bin/python3
"""Check if object is instance of/inherited from class."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance of or inherited from class.

    Args:
        obj: Object to check
        a_class: Class to compare against

    Returns:
        bool: True if obj is instance of or inherited from a_class,
              False otherwise
    """
    return isinstance(obj, a_class)
