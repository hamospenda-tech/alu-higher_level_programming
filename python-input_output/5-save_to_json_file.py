#!/usr/bin/python3
"""Module that saves an object to a text file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a text file.

    Args:
        my_obj: the object to serialize.
        filename (str): the path of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
