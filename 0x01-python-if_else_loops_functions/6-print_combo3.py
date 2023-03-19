#!/usr/bin/python3
# program to combine numbers such that they do not appear twice the same time
for i in range(0, 9):
    for n in range(i+1, 10):
        if i == 8 and n == 9:
            print("{}{}".format(i, n), end="")
        else:
            print("{}{}, ".format(i, n), end="")
print()
