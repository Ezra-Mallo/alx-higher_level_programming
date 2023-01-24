#!/usr/bin/python3
# 101-safe_function.py
# ezra.mallo@gmail.com
import sys


def safe_function(fct, *args):
    """Function that executes a function safely."""

    try:
        result = fct(args[0], args[1])
        return result
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
