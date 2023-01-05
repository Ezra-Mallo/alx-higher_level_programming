#!/usr/bin/python3

# 4-hidden_discovery.py
# ezra.mallo@gmail.com

if __name__ == "__main__":
    """Program that prints all the names defined by the compiled
    module hidden_4.pyc (please download it locally)."""

    import hidden_4 as a

    my_lists = dir(a)

    for my_list in my_lists:
        if my_list[0:2] != "__":
            print("{}".format(my_list))
