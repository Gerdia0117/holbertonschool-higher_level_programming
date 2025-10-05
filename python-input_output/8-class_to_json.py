#!/usr/bin/python3
"""Function that returns the dictionary description
of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object
    with only serializable attributes.

    Args:
        obj: Instance of a class.

    Returns:
        dict: Dictionary containing all attributes of obj.
    """
    return obj.__dict__.copy()
