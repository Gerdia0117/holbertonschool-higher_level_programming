#!/usr/bin/python3
"""
Module for reading and printing the contents of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to empty string.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
