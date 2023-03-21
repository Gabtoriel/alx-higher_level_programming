#!/usr/bin/python3
# program to check if a letter is in lowercase
def islower(c):
    letter_index = ord(c)
    if letter_index >= 97 and letter_index <= 122:
        return True
    else:
        return False
