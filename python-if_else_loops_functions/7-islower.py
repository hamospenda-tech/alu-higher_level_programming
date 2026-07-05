#!/usr/bin/python3
"""Module that defines islower"""


def islower(c):
    """Check if a character is lowercase using ord()"""
    return ord(c) >= 97 and ord(c) <= 122
