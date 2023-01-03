#!/usr/bin/python3
"""Program that prints the ASCII alphabet, in reverse order, alternating
    lowercase and uppercase (z in lowercase and Y in uppercase) ,
    not followed by a new line."""

# 100-print_tebahpla.pyi
# ezra.mallo@gmail.com

for xter in range(122, 96, -1):
    if xter % 2 == 0:
        print("{}".format(chr(xter)), end="")
    else:
        print("{}".format(chr(xter - 32)), end="")

