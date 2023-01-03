#!/usr/bin/python3

# 5-print_comb2.py
# ezra.mallo@gmail.comi

for num in range(99):
    if num != 98:
        print("{:02d},".format(num), end=" ")
    else:
        print("{:02d}".format(num))

