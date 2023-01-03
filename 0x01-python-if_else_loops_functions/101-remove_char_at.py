#!/usr/bin/python3

# 101-remove_char_at.p
# ezra.mallo@gmail.com


def remove_char_at(str, n):
    """Function that creates a copy of the string, removing the character 
        at the position n (not the Python way, the “C array index”)."""

    new_str = ""
    lenght = len(str)

    for i in range(0, lenght):
        if i != n:
            new_str = new_str + str[i]
        else:
            pass

    return (new_str)
