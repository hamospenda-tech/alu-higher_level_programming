#!/usr/bin/python3
"""Module that defines safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, integers only.

    Non-integer elements are skipped silently. All integers are
    printed on the same line followed by a newline.

    Returns the real number of integers printed.
    """
    count = 0
    i = 0
    try:
        while i < x:
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                pass
            i += 1
    except IndexError:
        pass
    print()
    return count
