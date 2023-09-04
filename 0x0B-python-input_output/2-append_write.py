#!/usr/bin/python3

"""Program that appends a given text to a file
creates it if it doesn't exist and returns the number
of characters written.
"""


def append_write(filename="", text=""):

    """Function that appends a given text to a file and
    returns the size written.

    >>> append_write("myfile2.txt", "Hello python input and output file handli\
ng2.")
    45
    """

    with open(filename, 'a', encoding='utf-8') as f:
        s = f.write(text)
        return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
