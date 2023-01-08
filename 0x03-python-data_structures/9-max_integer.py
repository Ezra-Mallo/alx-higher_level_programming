#!/usr/bin/python3
# 9-max_integer.py
# ezra.mallo@gmail.com


def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list."""

    maximum = 0
    for i in range(len(my_list)):
        if maximum <= my_list[i]:
            maximum = my_list[i]
    return maximum
