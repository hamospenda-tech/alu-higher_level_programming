#!/usr/bin/python3
"""Module that defines max_integer"""


def max_integer(my_list=[]):
    """Find the biggest integer of a list, without using max().
    Returns None if the list is empty"""
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number
    return biggest
