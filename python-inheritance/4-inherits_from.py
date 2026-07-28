#!/usr/bin/python3
"""Module that checks for strict (indirect) class inheritance."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class.

    The check excludes the case where obj's type is exactly a_class.

    Args:
        obj: any object.
        a_class: the class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
            False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
