#!/usr/bin/python3
# 8-multiple_returns.py
# ezra.mallo@gmail.com


def multiple_returns(sentence):
    """Function that returns a tuple with the length of a string 
        and its first character."""

    lenght = len(sentence)
    if lenght == 0:
        return (None)
    else:
        first_xter = sentence[0]

    return (lenght, first_xter)




