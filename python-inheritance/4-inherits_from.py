#!/usr/bin/python3
"""Check if object inherits (directly/indirectly) from class."""


def inherits_from(obj, a_class):
    """Check if object inherits from class (excluding direct instance).

    Args:
        obj: Object to check
        a_class: Class to compare against

    Returns:
        bool: True if obj's class inherits from a_class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
