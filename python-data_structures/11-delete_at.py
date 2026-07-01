#!/usr/bin/python3
"""Module that defines delete_at"""


def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list.
    If idx is negative or out of range, the list is unchanged"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[:] = my_list[:idx] + my_list[idx + 1:]
    return my_list
