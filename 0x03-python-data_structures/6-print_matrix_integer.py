#!/usr/bin/python3
#  6-print_matrix_integer.py
# ezra.mallo@gmail.com



def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers."""

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col < 2:
                print("{:d} ".format(matrix[row][col]), end="")
            elif col == 2:
                print("{:d}".format(matrix[row][col]))

#    print("\n")
