#!/usr/bin/python3
"""Student class module with JSON serialization and reloading.
"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                If None or not a list of strings, include all attributes.

        Returns:
            dict: Dictionary representation of the student.
        """
        student_dict = self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(a, str)
                                           for a in attrs):
            filtered = {k: v for k, v in student_dict.items() if k in attrs}
            return filtered
        return student_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
