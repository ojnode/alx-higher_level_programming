#!/usr/bin/python3
for j in range(10):
    for i in range(j + 1, 10):
        if j == 8 and i == 9:
            print("{}{}".format(j, i))
        else:
            print("{}{}".format(j, i), end=", ")
