#!/usr/bin/python3
"""Module that defines safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, integers only.

    Non-integer elements are skipped silently. All integers are
    printed on the same line followed by a newline.

    Returns the real number of integers printed.

    Raises an exception if x is bigger than the length of my_list.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
