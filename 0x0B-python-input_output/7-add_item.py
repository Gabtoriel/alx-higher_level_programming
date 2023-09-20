#!/usr/bin/python3

"""Script to update serialize and deserialize a python object.
to json string."""

import json, sys, os


filename = "add_item.json"

def main():

    """controls the serialization and deserialization of passed
    in command line arguments."""

    argv = sys.argv[1:]
    arr = []

    if len(argv) == 0 or len(argv) < 0:
        if os.path.getsize(filename) == 0:
            save_to_json_file(arr, filename)
    else:
        if os.path.getsize(filename) == 0:
            for arg in argv:
                arr.append(arg)
        else:
            arr = load_from_json_file(filename)
            for arg in argv:
                arr.append(arg)
        save_to_json_file(arr, filename)

def save_to_json_file(my_obj, filename):

    """Writes the json representation of an object to a file.

    >>> save_to_json_file({'a': 2, 'b': "hi"}, "myjson.txt")
    """

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)


def load_from_json_file(filename):

    """Accepts a json file as input and then converts the json
    string to a valid python object.

    >>> load_from_json_file('myjson.txt')
    {'a': 2, 'b': 'hi'}
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

main()
