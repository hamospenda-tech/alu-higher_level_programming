#!/usr/bin/python3
"""Module that defines add_tuple"""


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise, returning a tuple of 2 integers.
    Missing elements are treated as 0; extra elements beyond
    the first 2 are ignored"""
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
