#!/usr/bin/python3
"""Module that defines best_score"""


def best_score(a_dictionary):
    """Return the key with the biggest integer value.
    Returns None if no score found"""
    if not a_dictionary:
        return None
    best_key = None
    best_val = None
    for key, value in a_dictionary.items():
        if best_val is None or value > best_val:
            best_key = key
            best_val = value
    return best_key
