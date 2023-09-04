#!/usr/bin/python3

"""Program to print a square given the size."""


def print_square(size):

    """Program to print a square based on a given size.

       >>> print_square(5)
       #####
       #####
       #####
       #####
       #####

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    sq_font = "#"

    for y in range(size):
        for x in range(size):
            print(sq_font, end='')
        print()


if __name__ == "__main__":
    print_square(5)
