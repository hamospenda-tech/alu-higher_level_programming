#!/usr/bin/python3
"""Module that defines simple_delete"""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary. Does nothing if key doesn't exist"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
