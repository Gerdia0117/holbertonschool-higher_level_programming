#!/usr/bin/python3
"""
Module for appending a string to a text file and returning character count.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8).
    Returns number of characters added.

    Args:
        filename (str): Name of file to append to
        text (str): Text to append to file

    Returns:
        int: Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
