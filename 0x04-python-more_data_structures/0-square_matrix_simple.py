#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes square value of integers of a matrix"""

    sqr = lambda x: x*x
    matrix_result = [list(map(sqr, row)) for row in matrix]
    return matrix_result
