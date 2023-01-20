#!/usr/bin/python3


def roman_to_int(roman_string):
    rom_str = roman_string
    roman_dict = {
            'I': 1,
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

    while i < len(rom_str):
        """i+1 checks if their is the next string after i to avoid error
        roman_string[i:i+2] chend 2 cter for IX, IV, XL, CD, CM)"""
        if (i + 1) < len(rom_str) and (rom_str[i: i + 2]) in roman_dict:
            num += roman_dict[rom_str[i: i + 2]]
#           jump 2 xters
            i += 2
        else:
            num += roman_dict[rom_str[i]]
            i += 1
        return num
