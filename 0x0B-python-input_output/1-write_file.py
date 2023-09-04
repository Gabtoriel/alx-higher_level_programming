#!/usr/bin/python3

"""Program that writes a given text to a file
creates it if it doesn't exist and returns the number
of characters written.
"""


def write_file(filename="", text=""):

    """Function that writes a given text to a file and
    returns the size written.

    >>> write_file("myfile.txt", "Hello python input and output file handlin\
g2.")
    45
    """

    with open(filename, 'w', encoding='utf-8') as f:
        s = f.write(text)
        return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
