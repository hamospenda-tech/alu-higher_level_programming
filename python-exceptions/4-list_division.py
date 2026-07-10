#!/usr/bin/python3
"""Module that defines list_division."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element two lists.

    Returns a new list (length = list_length) with the results.
    Uses 0 wherever the division could not be performed.
    """
    new_list = []
    for i in range(list_length):
        try:
            element = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            element = 0
        except TypeError:
            print("wrong type")
            element = 0
        except IndexError:
            print("out of range")
            element = 0
        finally:
            new_list.append(element)
    return new_list
