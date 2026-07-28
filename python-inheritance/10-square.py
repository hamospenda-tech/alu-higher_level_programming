#!/usr/bin/python3
"""Module that defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
        """
        super().__init__(size, size)
