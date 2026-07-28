#!/usr/bin/python3
"""Module that returns the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: the object to serialize.

    Returns:
        str: the JSON representation of my_obj.
    """
    return json.dumps(my_obj)
