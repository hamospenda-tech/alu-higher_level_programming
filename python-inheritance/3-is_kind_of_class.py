#!/usr/bin/python3
"""Module that checks inheritance-inclusive instance membership."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a class derived from it.

    Args:
        obj: any object.
        a_class: the class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass
            of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
