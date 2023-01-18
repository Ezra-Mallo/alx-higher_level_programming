#!/usr/bin/python3
# 100-weight_average.py
# ezra.mallo@gmail.com

def weight_average(my_list=[]):
    a = b = 0
    for ind1, ind2 in my_list:
        a += ind1 * ind2
        b += ind2

    return (a/b)
