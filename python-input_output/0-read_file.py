#!/usr/bin/python3
"""Module that reads a text file and prints its contents to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout.

    Args:
        filename (str): the path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
