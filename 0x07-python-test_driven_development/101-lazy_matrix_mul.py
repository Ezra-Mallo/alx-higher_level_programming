#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """To multiply 2 matrices using NumPy

    Args:
        m_a: matrix
        m_b: matrix
    Return: matrix product

    """

    return (np.matmul(m_a, m_b))
