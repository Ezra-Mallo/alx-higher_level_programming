#!/usr/bin/python3

# 8-uppercase.py
# ezra.mallo@gmail.com

def uppercase(str):
    """Function that checks for uppercase character."""
    new_str =""
    lenght = len(str)

    for i in range(0, lenght):
        asci = ord(str[i])

        if asci >= 97 and asci <= 122:
            new_str =  new_str + chr(asci - 32)
        else:
            new_str =  new_str + chr(asci)

    print("{}".format(new_str))

