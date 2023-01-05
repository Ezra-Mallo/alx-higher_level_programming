#!/usr/bin/python3

# 0_add.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Simple calculator program for +, -, * & /"""

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
