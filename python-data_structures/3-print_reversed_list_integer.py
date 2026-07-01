#!/usr/bin/python3
"""Module that defines print_reversed_list_integer"""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line"""
    if my_list is None:
        return
    for number in my_list[::-1]:
        print("{:d}".format(number))
