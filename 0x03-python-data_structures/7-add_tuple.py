#!/usr/bin/python3

# 7-add_tuple.py
# ezra.mallo@gmail.com

def add_tuple(tuple_a=(), tuple_b=()):
    """Write a function that adds 2 tuples."""

    for i in len(tuple_a):
        for j in range(len(tuple_b)):
            print("{}".format(tuple_a[i, j]))
