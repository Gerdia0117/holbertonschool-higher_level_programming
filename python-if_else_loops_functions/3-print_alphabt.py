#!/usr/bin/python3
letters = [chr(i) for i in range(97, 123)
           if i != 101 and i != 113]
print("{}".format("".join(letters)), end="")
