#!/usr/bin/python3
"""Module that defines print_list_integer"""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line"""
    for number in my_list:
        print("{:d}".format(number))
