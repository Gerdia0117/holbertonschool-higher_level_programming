#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line"""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - 32)  # convert to uppercase
        print("{}".format(c), end="")
    print()
