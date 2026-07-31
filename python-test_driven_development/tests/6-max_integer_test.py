#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Max at the end of an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses default empty list"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """All negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        """Mix of negative and positive"""
        self.assertEqual(max_integer([-1, 5, -3]), 5)

    def test_duplicates(self):
        """List with duplicate values"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
