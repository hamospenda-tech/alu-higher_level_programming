#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the new Square (default 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
