#!/usr/bin/python3
"""
Module for creating Python objects from JSON files.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read

    Returns:
        object: Python data structure loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
