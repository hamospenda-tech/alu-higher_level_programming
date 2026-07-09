#!/usr/bin/python3
"""Module that defines print_sorted_dictionary"""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys (first level only)"""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
