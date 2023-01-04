#!/usr/bin/python3


# 9-print_last_digit.py
# ezra.mallo@gmail.com

def print_last_digit(number):
    """prints the last digit of a number."""

    num = abs(number)
    last_digit = num % 10

    print("{}".format(last_digit), end="")
    return last_digit
