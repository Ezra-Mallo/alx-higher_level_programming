#!/usr/bin/python3
# 5-text_indentation.py
#ezra.mallo@gmail.com


def text_indentation(text):
    """Prints a text with 2 new lines

    after each of these characters: .  ? and :

    Args:
        text: string
    Return: Nothing
    Raises:
        TypeError: text must be a string(if text not string)

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_list =[]
    start = 0

    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            my_list.append((start, i + 1))
            start = i + 2

    for list in my_list:
        print(text[list[0]:list[1]])
        print()
