#!/usr/bin/python3
"""Module that defines element_at"""


def element_at(my_list, idx):
    """Retrieve an element from a list by index, like in C"""
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
