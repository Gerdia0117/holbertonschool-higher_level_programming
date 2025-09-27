#!/usr/bin/python3
"""Defines a function that checks if an object is an instance
of a class that inherits from a specified class (directly or indirectly).
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits
    from a_class; otherwise False. Exact matches are not included.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
