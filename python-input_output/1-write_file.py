#!/usr/bin/python3
"""
Module for writing a string to a text file and returning character count.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters.

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file

    Returns:
        int: Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
