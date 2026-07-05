#!/usr/bin/python3
"""Module that defines islower"""


def islower(c):
    """Check if a character is lowercase using ord(), without str.upper() or str.isupper()"""
    return ord(c) >= 97 and ord(c) <= 122
