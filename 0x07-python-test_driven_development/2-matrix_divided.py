#!/usr/bin/python3
# 2-matrix_divided.py
# ezra.mallo@gmail.com


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.


    Args:
        matric (list of list): element must be integier or float. 
                Muat be a same size matrix. eg 2x2, 3x3
        div: integer or float

    Returns: result of matrix division with element in decima places

    Raises:
       1. if elements of matrix is not integer: TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

       2. if matrix is not same size: TypeError
                (Each row of the matrix must have the same size")

       3. if div is not integer or float: TypeError
                ("div must be a number")

       4. if div is zero: ZeroDivisionError 
                ("division by zero")

    """


    if not isinstance(matrix, list):
        raise TypeError\
                ("matrix must be a matrix (list of lisits) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError\
                ("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")

    new_mat = ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

    return new_mat
