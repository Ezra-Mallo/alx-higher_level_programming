#!/usr/bin/python3


def roman_to_int(roman_string):

    if (isinstance(roman_string, str)) is False or (roman_string is None):
        return (0)
    rom_dict = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                'IV': 4,
                'IX': 9,
                'XL': 40,
                'XC': 90,
                'CD': 400,
                'CM': 900}
    i = 0
    num = 0
    while i < len(roman_string):
        """i+1 checks if their is the next string after i to avoid error
        roman_string[i:i+2] chend 2 cter for IX, IV, XL, CD, CM)"""
        if i + 1 < len(roman_string) and (roman_string[i: i + 2]) in rom_dict:
            num += rom_dict[roman_string[i: i + 2]]
#           jump 2 xters
            i += 2
        else:
            num += rom_dict[roman_string[i]]
            i += 1
    return num
