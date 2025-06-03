#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): File to save the JSON data
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialize JSON data from a file to a Python dictionary.

    Args:
        filename (str): File containing JSON data

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, 'r') as f:
        return json.load(f)
