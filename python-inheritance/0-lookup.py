#!/usr/bin/python3
"""Module that provides a function to list an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: any object.

    Returns:
        list: the attributes and methods of obj.
    """
    return dir(obj)
