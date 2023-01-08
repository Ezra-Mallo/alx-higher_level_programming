#!/usr/bin/python3

# 5-no_c.py
# ezra.mallo@gmail.com

def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        xter = my_string[i]
        if xter != "c" and xter != "C":
            new_string += xter

    return new_string
