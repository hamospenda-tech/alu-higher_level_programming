#!/usr/bin/python3
"""Unittests for the Rectangle class"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for creating Rectangle instances"""

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertEqual(10, r.width)
        self.assertEqual(2, r.height)
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

    def test_three_args(self):
        r = Rectangle(10, 2, 3)
        self.assertEqual(3, r.x)

    def test_four_args(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(4, r.y)

    def test_five_args(self):
        r = Rectangle(10, 2, 3, 4, 89)
        self.assertEqual(89, r.id)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2)

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method"""

    def test_small(self):
        self.assertEqual(20, Rectangle(10, 2).area())

    def test_one_by_one(self):
        self.assertEqual(1, Rectangle(1, 1).area())

    def test_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method"""

    @staticmethod
    def capture(rect):
        buf = io.StringIO()
        sys.stdout = buf
        rect.display()
        sys.stdout = sys.__stdout__
        return buf.getvalue()

    def test_display_simple(self):
        self.assertEqual("##\n##\n", self.capture(Rectangle(2, 2)))

    def test_display_with_x(self):
        self.assertEqual("  ##\n  ##\n", self.capture(Rectangle(2, 2, 2)))

    def test_display_with_y(self):
        self.assertEqual("\n\n##\n", self.capture(Rectangle(2, 1, 0, 2)))


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method"""

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", str(r))

    def test_str_changed(self):
        r = Rectangle(4, 6, 2, 1, 12)
        r.width = 15
        self.assertEqual("[Rectangle] (12) 2/1 - 15/6", str(r))


class TestRectangleUpdate(unittest.TestCase):
    """Tests for the update method"""

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1, width=2, y=3, x=4, id=89)
        self.assertEqual("[Rectangle] (89) 4/3 - 2/1", str(r))

    def test_update_args_beats_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=1)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_bad_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_zero_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method"""

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(expected, r.to_dictionary())

    def test_to_dictionary_type(self):
        self.assertIsInstance(Rectangle(10, 2).to_dictionary(), dict)

    def test_to_dictionary_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
