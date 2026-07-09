#!/usr/bin/python3
"""Module that defines search_replace"""


def search_replace(my_list, search, replace):
    """Replace all occurrences of search with replace in a new list"""
    return list(map(lambda x: replace if x == search else x, my_list))
