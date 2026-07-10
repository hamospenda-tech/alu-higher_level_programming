#!/usr/bin/python3
"""Module that defines safe_print_integer."""


def safe_print_integer(value):
    """Print an integer using "{:d}".format().

    Returns True if value was successfully printed as an integer,
    False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
