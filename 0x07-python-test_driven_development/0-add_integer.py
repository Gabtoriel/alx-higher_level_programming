#!/usr/bin/python3

"""program to two integers.


   module: 0-add_integer
   function: add_integer
"""


def add_integer(a, b=98):

    """Routine to add two integers."""

    if (type(a) == str or type(a) == bool):
        raise TypeError("a must be an integer")
    elif (type(b) ==  str or type(b) == bool):
        raise TypeError("b must be an integer")
    if (type(a) == float):
        a =  int(a)
    if (type(b) == float):
        b = int(b)
    return a + b
