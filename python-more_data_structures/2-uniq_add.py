#!/usr/bin/python3
"""Module that defines uniq_add"""


def uniq_add(my_list=[]):
    """Add all unique integers in a list (each integer counted only once)"""
    seen = set()
    total = 0
    for num in my_list:
        if num not in seen:
            seen.add(num)
            total += num
    return total
