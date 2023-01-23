#!/usr/bin/python3
# 1-safe_print_integer.py
# ezra.mallo@gmail.com


def safe_print_integer(value):
    """Function that prints an integer with "{:d}".format()."""

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return (False)
