#!usr/bin/python3
# 6-print_sorted_dictionary.py
# ezra.mallo@gmail.com


def print_sorted_dictionary(a_dictionary):

    a_dic = a_dictionary.copy()
    for keys in sorted(a_dic.keys()):
        print('{}: {}'. format(keys, a_dic[keys]))
