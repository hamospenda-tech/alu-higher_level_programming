#!/usr/bin/python3
"""Module that defines print_matrix_integer"""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line, space-separated"""
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
