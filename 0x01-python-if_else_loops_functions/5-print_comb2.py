#!/usr/bin/python3
# program to print numbers from 0-99
for n in range(0, 100):
    if n == 99:
        print("{0:02}".format(n), end="")
    else:
        print("{0:02}, ".format(n), end="")
print()
