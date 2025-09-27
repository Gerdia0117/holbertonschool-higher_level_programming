#!/usr/bin/python3
"""Defines a function that checks if an object is an instance
of a specified class or a subclass of it.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherits
    from a_class; otherwise return False.
    """
    return isinstance(obj, a_class)
