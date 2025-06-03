#!/usr/bin/python3
"""
Script that adds command line arguments to a Python list and saves to a file.
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Main function to handle adding arguments to list and saving to file.
    """
    filename = "add_item.json"

    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
