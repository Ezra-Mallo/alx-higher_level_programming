#!/usr/bin/python3
# 100-weight_average.py
# ezra.mallo@gmail.com


def square_matrix_map(matrix=[]):

    if not isinstance(matrix, list) or len(matrix) == 0:
        return (0)

    result = (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
    return (result)
