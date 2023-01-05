#!/usr/bin/python3

# 3-infinite_add.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Program that prints the result of the addition of all arguments"""

    from sys import argv

    count = len(argv)
    total = 0
    for i in range(1, count):
        total += int(argv[i])

    print("{}".format(total))
