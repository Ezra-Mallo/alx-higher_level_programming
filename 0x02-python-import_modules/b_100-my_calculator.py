#!/usr/bin/python3

# 100-my_calculator.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Program that imports all functions from the file

    calculator_1.py and handles basic operations. """

    from calculator_1 import add, sub, mul, div
    from sys import argv

    count = len(argv)
    if (count-1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (count - 1) == 3:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif argv[2] == "/":
            print("{} / {}i = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
