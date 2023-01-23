#!/usr/bin/python3
# 2-safe_print_list_integers.py
# ezra.mallo@gmail.com


def safe_print_list_integers(my_list=[], x=0):
    """Function to print the first x elements of a list and only integers."""

    total = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total += 1

        except (ValueError, TypeError):
            continue
    print("")
    return total
