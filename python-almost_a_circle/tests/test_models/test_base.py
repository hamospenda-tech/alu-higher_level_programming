#!/usr/bin/python3
"""Unittests for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_auto_id_increments(self):
        """Consecutive instances without id get incrementing ids"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """An explicit id is assigned as-is"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_given_id_does_not_increment(self):
        """An explicit id does not consume a counter value"""
        b1 = Base()
        b2 = Base(1000)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_id_zero(self):
        """id=0 is not None, so it is assigned as-is"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_id(self):
        """Negative ids are assigned as-is"""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_nb_objects_private(self):
        """__nb_objects is private and not directly accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()


class TestBaseToJsonString(unittest.TestCase):
    """Test cases for the to_json_string static method"""

    def test_none_returns_empty_list_string(self):
        """None input returns the string []"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list_returns_empty_list_string(self):
        """Empty list input returns the string []"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_returns_string(self):
        """The return value is a str"""
        result = Base.to_json_string([{'id': 1}])
        self.assertIsInstance(result, str)

    def test_json_round_trip(self):
        """The JSON string parses back to the original list"""
        import json
        data = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        result = Base.to_json_string(data)
        self.assertEqual(json.loads(result), data)

    def test_multiple_dictionaries(self):
        """Works with several dictionaries in the list"""
        import json
        data = [{'id': 1}, {'id': 2}]
        self.assertEqual(json.loads(Base.to_json_string(data)), data)


class TestBaseSaveToFile(unittest.TestCase):
    """Test cases for the save_to_file class method"""

    def tearDown(self):
        """Remove files created by the tests"""
        import os
        for f in ["Rectangle.json", "Square.json"]:
            if os.path.exists(f):
                os.remove(f)

    def test_save_rectangles(self):
        """Saves a list of rectangles to Rectangle.json"""
        import json
        from models.rectangle import Rectangle
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            data = json.load(f)
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_filename_uses_class_name(self):
        """Squares are saved to Square.json"""
        import os
        from models.square import Square
        Square.save_to_file([Square(1, 0, 0, 1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_none(self):
        """None saves an empty list"""
        from models.rectangle import Rectangle
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        """An empty list saves []"""
        from models.rectangle import Rectangle
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_overwrites_existing_file(self):
        """An existing file is overwritten"""
        import json
        from models.rectangle import Rectangle
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        Rectangle.save_to_file([Rectangle(2, 4, 0, 0, 2)])
        with open("Rectangle.json") as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 2)


class TestBaseFromJsonString(unittest.TestCase):
    """Test cases for the from_json_string static method"""

    def test_none_returns_empty_list(self):
        """None input returns an empty list"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string_returns_empty_list(self):
        """Empty string input returns an empty list"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_round_trip(self):
        """from_json_string reverses to_json_string"""
        data = [{'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}]
        json_str = Base.to_json_string(data)
        self.assertEqual(Base.from_json_string(json_str), data)

    def test_returns_list(self):
        """The return value is a list"""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertIsInstance(result, list)


class TestBaseCreate(unittest.TestCase):
    """Test cases for the create class method"""

    def test_create_rectangle(self):
        """create returns a Rectangle matching the dictionary"""
        from models.rectangle import Rectangle
        r1 = Rectangle(3, 5, 1, 0, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r2), str(r1))

    def test_create_square(self):
        """create returns a Square matching the dictionary"""
        from models.square import Square
        s1 = Square(5, 2, 3, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s2), str(s1))

    def test_create_returns_new_instance(self):
        """The created instance is a different object"""
        from models.rectangle import Rectangle
        r1 = Rectangle(3, 5, 1, 0, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertFalse(r1 == r2)

    def test_create_type(self):
        """create returns an instance of the calling class"""
        from models.rectangle import Rectangle
        from models.square import Square
        r = Rectangle.create(**{'id': 1, 'width': 2, 'height': 3})
        s = Square.create(**{'id': 1, 'size': 2})
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(s, Square)


class TestBaseLoadFromFile(unittest.TestCase):
    """Test cases for the load_from_file class method"""

    def tearDown(self):
        """Remove files created by the tests"""
        import os
        for f in ["Rectangle.json", "Square.json"]:
            if os.path.exists(f):
                os.remove(f)

    def test_load_rectangles(self):
        """Saved rectangles load back with the same attributes"""
        from models.rectangle import Rectangle
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(o) for o in loaded], [str(r1), str(r2)])
        for o in loaded:
            self.assertIsInstance(o, Rectangle)

    def test_load_squares(self):
        """Saved squares load back with the same attributes"""
        from models.square import Square
        s1 = Square(5, 0, 0, 5)
        s2 = Square(7, 9, 1, 6)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(o) for o in loaded], [str(s1), str(s2)])
        for o in loaded:
            self.assertIsInstance(o, Square)

    def test_missing_file_returns_empty_list(self):
        """A missing file returns an empty list"""
        from models.rectangle import Rectangle
        self.assertEqual(Rectangle.load_from_file(), [])
