#!/usr/bin/python3
"""Module that defines fizzbuzz"""


def fizzbuzz():
    """Print numbers 1 to 100 separated by spaces,
    replacing multiples of 3 with Fizz, 5 with Buzz, both with FizzBuzz"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
