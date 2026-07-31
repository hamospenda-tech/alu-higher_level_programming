#!/usr/bin/python3
"""Unittests for the Square class"""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    """Tests for creating Square instances"""

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_one_arg(self):
        s = Square(10)
        self.assertEqual(10, s.size)
        self.assertEqual(0, s.x)
        self.assertEqual(0, s.y)

    def test_two_args(self):
        s = Square(10, 2)
        self.assertEqual(2, s.x)

    def test_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(1, s.size)
        self.assertEqual(2, s.x)
        self.assertEqual(3, s.y)

    def test_four_args(self):
        s = Square(10, 2, 3, 89)
        self.assertEqual(89, s.id)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquareSize(unittest.TestCase):
    """Tests for the size property"""

    def test_getter(self):
        self.assertEqual(5, Square(5).size)

    def test_setter(self):
        s = Square(5)
        s.size = 8
        self.assertEqual(8, s.size)
        self.assertEqual(8, s.width)
        self.assertEqual(8, s.height)

    def test_setter_string(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "invalid"

    def test_setter_zero(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquareArea(unittest.TestCase):
    """Tests for the area method"""

    def test_area(self):
        self.assertEqual(100, Square(10).area())

    def test_area_after_resize(self):
        s = Square(3)
        s.size = 7
        self.assertEqual(49, s.area())


class TestSquareStr(unittest.TestCase):
    """Tests for the __str__ method"""

    def test_str(self):
        s = Square(5, 2, 3, 12)
        self.assertEqual("[Square] (12) 2/3 - 5", str(s))

    def test_str_after_update(self):
        s = Square(5, 2, 3, 12)
        s.size = 9
        self.assertEqual("[Square] (12) 2/3 - 9", str(s))


class TestSquareUpdate(unittest.TestCase):
    """Tests for the update method"""

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(size=2, x=3, y=4, id=89)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_bad_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_zero_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method"""

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        expected = {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(expected, s.to_dictionary())

    def test_to_dictionary_type(self):
        self.assertIsInstance(Square(10).to_dictionary(), dict)

    def test_to_dictionary_with_arg(self):
        with self.assertRaises(TypeError):
            Square(10).to_dictionary(1)


class TestSquareSaveToFile(unittest.TestCase):
    """Tests for the save_to_file method"""

    @classmethod
    def tearDown(cls):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        Square.save_to_file([Square(3, 5, 1, 4)])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()


if __name__ == "__main__":
    unittest.main()
