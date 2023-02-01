#!/usr/bin/python3
# 100-matrix_mul.py
# ezra.mallo@gmail.com

def matrix_mul(m_a, m_b):
    """ multiply 2 matrix

    Argv:
        m_a: matrix
        m_b = matriici


    """
    mat = []
    result = 0
    for row in m_a:
        row = []
        for col in m_b:
            result += col * row
        print (row[0], col[0])
