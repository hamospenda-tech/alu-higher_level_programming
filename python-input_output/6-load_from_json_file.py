#!/usr/bin/python3
"""Module that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create and return an object from a JSON file.

    Args:
        filename (str): the path of the JSON file to read.

    Returns:
        The Python object represented by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
