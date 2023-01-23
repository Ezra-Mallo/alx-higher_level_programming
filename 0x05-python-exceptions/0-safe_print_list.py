#!/usr/bin/python3
# 0-safe_print_list.py
# ezra.mallo@gmail.com


def safe_print_list(my_list=[], x=0):
    """Function that prints x elements of a list."""

    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break

    print("")
    return num
