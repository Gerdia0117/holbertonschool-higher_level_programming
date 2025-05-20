#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -1, -11]), -1)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-10, 15, 0, -7]), 15)

    def test_all_equal(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.8, 0.3]), 2.8)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 3.5, 2]), 3.5)

    def test_string_list(self):
        self.assertEqual(max_integer(["apple", "banana", "zebra"]), "zebra")

    def test_list_with_strings_and_ints(self):
        with self.assertRaises(TypeError):
            max_integer(["one", 2, "three"])
