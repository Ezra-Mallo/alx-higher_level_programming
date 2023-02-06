#!/usr/bin/python3
# 1-my_list.py
# ezra.mallo@gmail.com


class MyList(list):
    """ A class MyList that inherits from list    """

    def print_sorted(self):
        """Print listed as sorted
            Args:
                obj: Objects
            Returns: List
        """

        print(sorted(self))
