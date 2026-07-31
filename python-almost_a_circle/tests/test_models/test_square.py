#!/usr/bin/python3
"""Unittests for models/square.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_inheritance(self):
        """Square is a Rectangle and a Base"""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_size_sets_both_dimensions(self):
        """width and height both equal size"""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_str(self):
        """String representation uses [Square] and a single size"""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2, 0, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        s3 = Square(3, 1, 3, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")

    def test_area(self):
        """Inherited area works: size squared"""
        self.assertEqual(Square(5, 0, 0, 1).area(), 25)
        self.assertEqual(Square(2, 2, 0, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3, 3).area(), 9)

    def test_display_inherited(self):
        """Inherited display works with x and y offsets"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Square(2, 2, 0, 2).display()
        self.assertEqual(out.getvalue(), "  ##\n" * 2)

    def test_validation_inherited(self):
        """Rectangle validation applies to size, x and y"""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -1)
        with self.assertRaises(TypeError):
            Square(5, 0, "3")


if __name__ == '__main__':
    unittest.main()


class TestSquareSize(unittest.TestCase):
    """Test cases for the Square size property"""

    def test_size_getter(self):
        """size returns the width"""
        s = Square(5, 0, 0, 1)
        self.assertEqual(s.size, 5)

    def test_size_setter_updates_both(self):
        """Assigning size updates width and height together"""
        s = Square(5, 0, 0, 1)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_type_validation(self):
        """Non-integer size raises the width TypeError message"""
        s = Square(5)
        with self.assertRaises(TypeError) as cm:
            s.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_size_value_validation(self):
        """Non-positive size raises the width ValueError message"""
        s = Square(5)
        with self.assertRaises(ValueError) as cm:
            s.size = 0
        self.assertEqual(str(cm.exception), "width must be > 0")


class TestSquareUpdate(unittest.TestCase):
    """Test cases for the Square update method"""

    def test_update_args_progressive(self):
        """Positional args update id, size, x, y in order"""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Keyword args update attributes in any order"""
        s = Square(2, 3, 4, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/4 - 2")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=8, id=89, y=2)
        self.assertEqual(str(s), "[Square] (89) 12/2 - 8")

    def test_update_size_updates_both_dimensions(self):
        """update via size keeps width and height in sync"""
        s = Square(5, 0, 0, 1)
        s.update(1, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)

    def test_args_skip_kwargs(self):
        """kwargs are ignored when args are present"""
        s = Square(5, 0, 0, 1)
        s.update(10, size=99)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

    def test_update_validation(self):
        """size validation applies through update"""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "2")
        with self.assertRaises(ValueError):
            s.update(1, -2)


class TestSquareToDictionary(unittest.TestCase):
    """Test cases for the Square to_dictionary method"""

    def test_to_dictionary(self):
        """Dictionary contains id, size, x and y"""
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(),
                         {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_to_dictionary_type(self):
        """The return value is a dict"""
        self.assertIsInstance(Square(1).to_dictionary(), dict)

    def test_no_width_height_keys(self):
        """The dictionary uses size, not width/height"""
        d = Square(5).to_dictionary()
        self.assertNotIn('width', d)
        self.assertNotIn('height', d)

    def test_dictionary_feeds_update(self):
        """The dictionary can recreate a square via update(**dict)"""
        s1 = Square(10, 2, 1, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s2), str(s1))
