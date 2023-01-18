#!/usr/bin/python3
# 100-weight_average.py
# ezra.mallo@gmail.com

def weight_average(my_list=[]):
    """Function that returns the weighted average of all
    integers tuple (<score>, <weight>)"""

    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    a = b = 0
    for ind1, ind2 in my_list:
        a += ind1 * ind2
        b += ind2

    return (a/b)
