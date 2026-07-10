#!/usr/bin/python3
"""Module that defines safe_print_division."""


def safe_print_division(a, b):
    """Divide a by b and print the result inside a finally block.

    Returns the result of the division, or None if it failed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
