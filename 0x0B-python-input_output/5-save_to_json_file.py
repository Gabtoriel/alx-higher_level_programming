#!/usr/bin/python3

"""Program that takes in a python obj and writes the
   json representation to a given file."""


import json

def save_to_json_file(my_obj, filename):

    """Writes the json representation of an object to a file.

    >>> save_to_json_file({'a': 2, 'b': "hi"}, "myjson.txt")
    """

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
