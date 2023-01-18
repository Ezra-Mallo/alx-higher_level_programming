#!/usr/bin/python3


def roman_to_int(roman_string):
   res = ""
   table = [
           (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
           (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
           (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
           ]

   for ind, roman in table:
       d, m = divmod(roman_string, ind)
      res += roman * d
      num = m

   return res

   import roman
    return (roman.fromRoman(romman_string))
