#!/usr/bin/python3

"""Program to convert a python string to a object."""


import json


def to_json_string(my_obj):

    """Returns the json representation of a given
    serializable object.

    >>> to_json_string([0,1,2,3,4])
    '[0, 1, 2, 3, 4]'
    """

    s = json.dumps(my_obj)
    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
