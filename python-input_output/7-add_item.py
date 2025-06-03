#!/usr/bin/python3
"""
Script that adds command line arguments to a Python list and saves to a file.
"""
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def main():
    """
    Main function to handle adding arguments to list and saving to file.
    """
    filename = "add_item.json"

    # Load existing list or create new one
    if path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add command line arguments (excluding script name)
    items.extend(sys.argv[1:])

    # Save updated list to file
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
