#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: the size of the new Square (default 0).
            position: the position of the new Square (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(n) is int for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#'.

        Prints an empty line if size is 0. Uses position to add
        vertical blank lines and horizontal spaces before each row,
        without trailing spaces after the square.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
