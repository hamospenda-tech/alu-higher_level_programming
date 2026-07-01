#!/usr/bin/python3
"""Module that defines replace_in_list"""


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position, like in C"""
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
