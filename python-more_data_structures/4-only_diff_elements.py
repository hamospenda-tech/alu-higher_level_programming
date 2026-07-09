#!/usr/bin/python3
"""Module that defines only_diff_elements"""


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set"""
    return set_1 ^ set_2
