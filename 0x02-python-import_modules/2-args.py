#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()
argStr = '{:d} argument'
arg = len(sts.argv) - 1
if arg == 0:
    argStr += 's.'
elif arg == 1:
    argStr += '.'
else:
    argStr += 's:'
print("argStr".format(arg))

i = 0
for strg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, strg))
    i += 1
