#!/usr/bin/python3
"""Module that defines print_last_digit"""


def print_last_digit(number):
    """Print the last digit of a number and return it"""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
