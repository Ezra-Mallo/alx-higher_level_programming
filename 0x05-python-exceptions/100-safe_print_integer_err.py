#!/usr/bin/python3
# 100-safe_print_integer_err.py
# ezra.mallo@gmail.com
import sys


def safe_print_integer_err(value):
    """Function that prints an integer.

    Args: value can be any type (integer, string, etc.)

    Func: The integer should be printed followed by a new line
    Returns: True if value has been correctly printed (an integer)
             False if not integer and prints the error precede by Exception:

    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to use type()"""

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
