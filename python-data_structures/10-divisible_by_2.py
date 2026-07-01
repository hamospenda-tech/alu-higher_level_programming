#!/usr/bin/python3
"""Module that defines divisible_by_2"""


def divisible_by_2(my_list=[]):
    """Return a new list of the same size, with True/False at each
    position depending on whether the original integer is a multiple of 2"""
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
