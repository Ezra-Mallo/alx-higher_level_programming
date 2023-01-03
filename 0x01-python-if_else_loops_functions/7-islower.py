#!/usr/bin/python3

# 7-islower.py
# ezra.mallo@gmail.com

def islower(c):
    """Function that checks for lowercase character."""

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
