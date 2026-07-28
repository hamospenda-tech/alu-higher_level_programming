#!/usr/bin/python3
"""Module that writes a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write a string to a text file, overwriting any existing content.

    Args:
        filename (str): the path of the file to write to.
        text (str): the string to write.

    Returns:
        int: the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
