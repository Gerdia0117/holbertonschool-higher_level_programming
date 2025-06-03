#!/usr/bin/python3
"""
Module for defining a Student class with serialization
and deserialization capabilities.
"""


class Student:
    """
    A class that represents a student with serialization
    and deserialization methods.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a filtered dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to include

        Returns:
            dict: Dictionary containing the requested student attributes
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
