#!/usr/bin/python3

"""Program to read a file in utf-8 encoding and
   then prints it out.
"""


def read_file(filename=""):

    """function that reads all the contents of a file.

    >>> read_file("myfile.txt")
    Hello python input and output file handling.
    """

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
