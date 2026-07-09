#!/usr/bin/python3
"""Module that defines square_matrix_simple"""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix.
    Returns a new matrix of the same size, original is not modified"""
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))

