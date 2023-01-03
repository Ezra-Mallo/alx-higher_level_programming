#!/usr/bin/python3
"""Prints the ASCII alphabet, in lowercase, not followed by a new line."""

# 4-print_hexa.py
# ezra.mallo@gmail.com

for num in range(99):
    print("{:02d} = {:#02x}".format(num, num))
