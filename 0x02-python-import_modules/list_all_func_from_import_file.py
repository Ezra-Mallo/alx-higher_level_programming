#!/usr/bin/python3

# 100-my_calculator.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Program that imports all functions in module or file. """

    import sys as a
    import calculator_1 as b
    import string as c
    import math as d
    import random as e
    import builtins as f

    a_lists = dir(a)
    b_lists = dir(b)
    c_lists = dir(c)
    d_lists = dir(d)
    e_lists = dir(e)
    f_lists = dir(f)
    k = 0
    j = 0

    print("\n********************* sys   *************************")
    for a_list in a_lists:
        if a_list[:2] != "__":
            k = k + 1
            print("{}: {}".format(k, a_list))

    print("\n********************* calculator   *************************")
    for b_list in b_lists:
        if b_list[:2] != "__":
            j += 1
            print("{}: {}".format(j, b_list))

    print("\n********************* string   *************************")
    for c_list in c_lists:
        if c_list[:2] != "__":
            j += 1
            print("{}: {}".format(j, c_list))
    print("\n********************* maths   *************************")
    j = 0
    for d_list in d_lists:
        if d_list[:2] != "__":
            j += 1
            print("{}: {}".format(j, d_list))
    print("\n********************* random  *************************")
    j = 0
    for e_list in e_lists:
        if e_list[:2] != "__":
            j += 1
            print("{}: {}".format(j, e_list))
    print("\n********************* builtins   *************************")
    j = 0
    for f_list in f_lists:
        if f_list[:2] != "__":
            j += 1
            print("{}: {}".format(j, f_list))
