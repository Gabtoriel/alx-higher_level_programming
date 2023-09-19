#!/usr/bin/python3

"""Program that takes in a json string and returns a python object."""


import json

def from_json_string(my_str):

    """Accepts a json string and returns a python object.

    >>> from_json_string('[0, 1, 2, 3]')
    [0, 1, 2, 3]
    """

    obj = json.loads(my_str)
    return obj


if __name__ == "__main__":
    import doctest
    doctest.testmod()
