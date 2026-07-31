#!/usr/bin/python3
"""Module that defines the Square class, inheriting from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, a Rectangle with equal width and height"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): size of the square (width and height).
            x (int): horizontal offset.
            y (int): vertical offset.
            id (int): id passed up to the Base constructor.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size, assigning width then height with the same value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes via no-keyword args or key-worded args.

        Args:
            *args: values in the order id, size, x, y.
            **kwargs: key/value pairs of attributes to update,
                skipped if args exists and is not empty.
        """
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
