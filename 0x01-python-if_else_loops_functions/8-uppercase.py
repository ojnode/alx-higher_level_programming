#!/usr/bin/python3
def uppercase(c):
    for char in c:
        if ord(c) >= 97 and ord(c) <= 122:
            char = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
