#!/usr/bin/python3
"""Prints the ASCII alphabet, in lowercase, not followed by a new line."""

# 3-print_alphabt.py
# ezra.mallo@gmail.com

for xter in range(97, 123):
    if xter != 101 and xter != 113:
        print("{}".format(chr(xter)), end="")
