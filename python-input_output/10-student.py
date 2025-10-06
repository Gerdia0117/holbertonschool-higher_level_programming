#!/usr/bin/python3
"""Student class module with optional attribute filtering
"""


class Student:
    """Defines a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                If None or not a list of strings, include all attributes.

        Returns:
            dict: Dictionary representation of the student.
        """
        student_dict = self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered_dict = {k: v for k, v in student_dict.items() if k in attrs}
            return filtered_dict
        return student_dict
