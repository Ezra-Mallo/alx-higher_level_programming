#!/usr/bin/python3
# 101-square_matrix_map.py
# ezra.mallo@gmail.com


def square_matrix_map(matrix=[]):
    """Function that computes the square value
    of all integers of a matrix using map"""

    if not isinstance(matrix, list) or len(matrix) == 0:
        return (0)

    result = (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
    return (result)
