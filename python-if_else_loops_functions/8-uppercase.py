#!/usr/bin/python3
"""Module that defines uppercase"""


def uppercase(str):
    """Print a string in uppercase followed by a new line,
    without using str.upper() or str.isupper()"""
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print("{}".format(result))
