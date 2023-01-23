#!/usr/bin/python3
# 3-safe_print_division.py
# ezra.mallo@gmail.com


def safe_print_division(a, b):
    """.Write a function that divides 2 integers and prints the result."""

    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
            return None
    return result
