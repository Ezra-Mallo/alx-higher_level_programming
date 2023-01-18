#!/usr/bin/python3
# 10-best_score.py
# ezra.mallo@gmail.com


def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value."""

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    highest_score = 0
    for index in a_dictionary:
        score = a_dictionary[index]
        if highest_score < score:
            highest_key = index
            highest_score = score
    return (highest_score)
