#!/usr/bin/python3
"""
This module defines a function that prints a formatted full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
        >>> try:
        ...     say_my_name(12, "White")
        ... except Exception as e:
        ...     print(e)
        first_name must be a string
        >>> try:
        ...     say_my_name("John", None)
        ... except Exception as e:
        ...     print(e)
        last_name must be a string
        >>> say_my_name("Alice", "")
        My name is Alice
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = "{}{}".format(first_name, " " + last_name if last_name else " ")
    print("My name is {}".format(name))
