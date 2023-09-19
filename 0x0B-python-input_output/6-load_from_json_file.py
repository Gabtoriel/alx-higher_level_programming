#!/usr/bin/python3

"""Program to load a json string from a file and convert
   it to python object."""


import json

def load_from_json_file(filename):

    """Accepts a json file as input and then converts the json
    string to a valid python object.

    >>> load_from_json_file('myjson.txt')
    {'a': 2, 'b': 'hi'}
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
   import doctest
   doctest.testmod()
