#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): the number of rows of the triangle.

    Returns:
        list: a list of lists representing Pascal's triangle of n
            rows, or an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
