#!/usr/bin/python3
"""Module containing the lookup function."""


def lookup(obj):
    """Return a list of available attributes and methods of a object
    
    Args:
        obj: The object to inspect.
        
    Return:
        list: A list of strings representing the attribute and methods.
    """
    return dir(obj)
