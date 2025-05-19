#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Return a new list with all values multiplied by the given number."""
    return list(map(lambda x: x * number, my_list))
