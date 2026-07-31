#!/usr/bin/python3
"""Unittests for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_inherits_from_base(self):
        """Rectangle is a subclass of Base"""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_auto_id(self):
        """Rectangles without id get incrementing ids from Base"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_given_id(self):
        """An explicit id is assigned as-is"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_attributes_assigned(self):
        """All attributes are stored and readable via getters"""
        r = Rectangle(10, 2, 1, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def test_default_x_y(self):
        """x and y default to 0"""
        r = Rectangle(5, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_setters_update_values(self):
        """Setters update the private attributes"""
        r = Rectangle(1, 1)
        r.width = 20
        r.height = 30
        r.x = 2
        r.y = 4
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 4)

    def test_attributes_private(self):
        """The underlying attributes are private (name mangled)"""
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            print(r.__width)


if __name__ == '__main__':
    unittest.main()


class TestRectangleValidation(unittest.TestCase):
    """Test cases for Rectangle attribute validation"""

    def test_width_not_integer(self):
        """Non-integer width raises TypeError with the right message"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_width_not_positive(self):
        """Zero or negative width raises ValueError"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(-10, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_not_positive(self):
        """Zero or negative height raises ValueError"""
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, -2)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_validation(self):
        """x must be an integer >= 0"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, {})
        self.assertEqual(str(cm.exception), "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_validation(self):
        """y must be an integer >= 0"""
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")
        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_setter_validation_after_creation(self):
        """Setters validate on reassignment too"""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}


class TestRectangleArea(unittest.TestCase):
    """Test cases for the Rectangle area method"""

    def test_area(self):
        """Area is width * height"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_one_by_one(self):
        """Smallest valid rectangle"""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_after_update(self):
        """Area reflects updated dimensions"""
        r = Rectangle(3, 2)
        r.width = 5
        r.height = 4
        self.assertEqual(r.area(), 20)


class TestRectangleDisplay(unittest.TestCase):
    """Test cases for the Rectangle display method"""

    def test_display_4x6(self):
        """Displays 6 rows of 4 # characters"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Rectangle(4, 6).display()
        self.assertEqual(out.getvalue(), "####\n" * 6)

    def test_display_2x2(self):
        """Displays 2 rows of 2 # characters"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Rectangle(2, 2).display()
        self.assertEqual(out.getvalue(), "##\n##\n")

    def test_display_1x1(self):
        """Displays a single #"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Rectangle(1, 1).display()
        self.assertEqual(out.getvalue(), "#\n")


class TestRectangleStr(unittest.TestCase):
    """Test cases for the Rectangle __str__ method"""

    def test_str_full_args(self):
        """String representation with all arguments given"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_partial_args(self):
        """String representation with default y and auto id"""
        r = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_str_defaults(self):
        """String representation with default x and y"""
        r = Rectangle(3, 2, 0, 0, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 0/0 - 3/2")


class TestRectangleDisplayXY(unittest.TestCase):
    """Test cases for display with x and y offsets"""

    def test_display_with_x_and_y(self):
        """y adds blank lines before, x adds spaces before each row"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Rectangle(2, 3, 2, 2).display()
        self.assertEqual(out.getvalue(), "\n\n" + ("  ##\n" * 3))

    def test_display_with_x_only(self):
        """x offset only, no leading blank lines"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Rectangle(3, 2, 1, 0).display()
        self.assertEqual(out.getvalue(), " ###\n" * 2)

    def test_display_no_offset(self):
        """Original behavior preserved when x=0 and y=0"""
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            Rectangle(2, 2).display()
        self.assertEqual(out.getvalue(), "##\n##\n")


class TestRectangleUpdate(unittest.TestCase):
    """Test cases for the Rectangle update method"""

    def test_update_progressive(self):
        """Each additional argument updates the next attribute in order"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        """No arguments leaves the rectangle unchanged"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_validation_still_applies(self):
        """update goes through setters, so validation still fires"""
        r = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            r.update(89, -2)
        with self.assertRaises(TypeError):
            r.update(89, 2, "3")

    def test_update_extra_args_ignored(self):
        """Arguments beyond the 5 attributes are ignored"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5, 999)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Test cases for update with key-worded arguments"""

    def test_update_kwargs_progressive(self):
        """Keyword updates in any order"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_args_take_priority_over_kwargs(self):
        """kwargs are skipped when args is not empty"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, width=5)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_kwargs_validation_still_applies(self):
        """Keyword updates still go through setters"""
        r = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            r.update(width=-5)

    def test_unknown_kwargs_ignored(self):
        """Unknown attribute names are silently ignored"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(hello=99)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleToDictionary(unittest.TestCase):
    """Test cases for the Rectangle to_dictionary method"""

    def test_to_dictionary(self):
        """Dictionary contains the 5 expected key/value pairs"""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 1,
                          'height': 2, 'width': 10})

    def test_to_dictionary_type(self):
        """The return value is a dict"""
        r = Rectangle(1, 1)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_dictionary_feeds_update(self):
        """The dictionary can recreate a rectangle via update(**dict)"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r2), str(r1))

    def test_dictionary_is_a_copy(self):
        """Modifying the dict does not affect the rectangle"""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        d['width'] = 99
        self.assertEqual(r.width, 10)
