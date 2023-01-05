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

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    print("{} {} {} = {}".format(a, op, b, operators[op](a, b)))
