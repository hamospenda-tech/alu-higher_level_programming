#!/usr/bin/python3
"""Module that defines new_in_list"""


def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position,
    without modifying the original list"""
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
