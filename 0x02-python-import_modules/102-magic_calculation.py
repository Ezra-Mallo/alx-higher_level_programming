#!/usr/bin/pythom3
# 102-magic_calculation.py
# ezra.mallo@gmail.com


def magic_calculation(a, b):
    """Python function def magic_calculation(a, b):

    that does exactly the same as the following Python bytecode:"""
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
