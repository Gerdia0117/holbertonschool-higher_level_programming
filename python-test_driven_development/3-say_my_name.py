#!/usr/bin/python3
"""
A module with a function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Always include both placeholders with a space, even if last_name is empty
    print("My name is {} {}".format(first_name, last_name))
