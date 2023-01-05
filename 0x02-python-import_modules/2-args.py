#!/usr/bin/python3

# 2_argv.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Program that prints the number of and the list of its arguments."""

    from sys import argv

    count = len(argv)
    print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{}: {}".format(i, argv[i]))
