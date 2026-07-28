#!/usr/bin/python3
"""Module that appends a string to the end of a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file, creating it if needed.

    Args:
        filename (str): the path of the file to append to.
        text (str): the string to append.

    Returns:
        int: the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
