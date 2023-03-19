#!/usr/bin/python3
# program to print the letters of the alphabet except e and q
for char in range(97, 123):
    if char == 101 or char == 113:
        continue
    print("{}".format(chr(char), end="")
