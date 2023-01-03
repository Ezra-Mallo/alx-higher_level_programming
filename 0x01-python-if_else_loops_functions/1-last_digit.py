#!/usr/bin/python3
"""This program will assign a random signed number to the variable number
   each time it is executed. Complete the source code in order to print the
   last digit of the number stored in the variable number. """

# 1-last_digit.py
# ezra.mallo@gmail.com

import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = (-1 * number) % 10
    digit = -digit
else:
    digit = number % 10

print(f"Last digit of {number} is {digit} ", end="")

if digit > 5:
        print("and is greater than 5")
elif digit == 0:
        print("and is 0")
elif digit < 6 and digit != 0:
        print("and is less than 6 and not 0")
