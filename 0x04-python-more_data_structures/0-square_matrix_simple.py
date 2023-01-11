#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes square value of integers of a matrix"""

    matrix_result = [list(map(lambda x:x*x, row)) for row in matrix]
    return matrix_result
