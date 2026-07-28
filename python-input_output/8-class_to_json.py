#!/usr/bin/python3
"""Module that returns the dictionary description of a simple object."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization.

    Args:
        obj: an instance of a Class whose attributes are all
            serializable (list, dict, str, int, and bool).

    Returns:
        dict: the attributes of obj.
    """
    return obj.__dict__
