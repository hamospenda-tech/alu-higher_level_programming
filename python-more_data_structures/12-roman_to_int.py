#!/usr/bin/python3
"""Module that defines roman_to_int"""


def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer.
    Returns 0 if roman_string is not a string or is None"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(roman_string):
        curr = values[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total
