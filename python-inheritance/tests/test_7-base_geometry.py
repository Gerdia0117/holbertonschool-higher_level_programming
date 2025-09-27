#!/usr/bin/python3
"""Unittest for 7-base_geometry.py"""
import unittest
from io import StringIO
import sys

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class TestBaseGeometry(unittest.TestCase):
    def setUp(self):
        self.bg = BaseGeometry()

    def test_area_not_implemented(self):
        with self.assertRaises(Exception) as cm:
            self.bg.area()
        self.assertEqual(str(cm.exception), "area() is not implemented")

    def test_integer_validator_valid(self):
        try:
            self.bg.integer_validator("width", 10)
            self.bg.integer_validator("height", 1)
        except Exception:
            self.fail("integer_validator raised an exception for valid input")

    def test_integer_validator_type_error(self):
        test_cases = [
            ("str", "John"),
            ("float", 3.14),
            ("none", None),
            ("list", [1, 2, 3]),
            ("dict", {"key": 1}),
            ("tuple", (4,)),
            ("bool", True),
            ("set", {1, 2}),
        ]
        for name, value in test_cases:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as cm:
                    self.bg.integer_validator(name, value)
                self.assertEqual(str(cm.exception), f"{name} must be an integer")

    def test_integer_validator_value_error(self):
        test_cases = [
            ("zero", 0),
            ("negative", -5),
        ]
        for name, value in test_cases:
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as cm:
                    self.bg.integer_validator(name, value)
                self.assertEqual(str(cm.exception), f"{name} must be greater than 0")

    def test_integer_validator_missing_arguments(self):
        with self.assertRaises(TypeError):
            self.bg.integer_validator()
        with self.assertRaises(TypeError):
            self.bg.integer_validator("age")
        with self.assertRaises(TypeError):
            self.bg.integer_validator(value=5)


if __name__ == '__main__':
    unittest.main()
