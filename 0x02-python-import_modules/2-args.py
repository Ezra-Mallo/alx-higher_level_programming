#!/usr/bin/python3

# 2_argv.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Program that prints the number of and the list of its arguments."""

    from sys import argv

    count = len(argv)
    if (count-1) == 1:
        print("{} argument".format(count - 1), end="")
    else:
        print("{} arguments".format(count - 1), end="")

    if (count - 1) == 0:
        print(".")
    else:
        print(":")

    for i in range(1, count):
        print("{}: {}".format(i, argv[i]))
