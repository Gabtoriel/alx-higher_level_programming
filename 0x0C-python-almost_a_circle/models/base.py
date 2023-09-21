#!/usr/bin/python3

"""Program to create the base class of the rectangle and
   square objects.
"""


import json


class Base:

    """The base class of the rectangle and square object."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):

        """Class method to save the json string representation of an object
        to a file using the class name."""

        if list_objs is None or len(list_objs) == 0:
            with open("{}.json".format(cls), 'w') as f:
                json.dump([], f)
        else:
            objs = [obj.to_dictionary() for obj in list_objs]
            js_obj = cls.to_json_string(objs)
            with open("{}.json".format(cls), 'w') as f:
                json.dump(js_objs, f)

    @staticmethod
    def to_json_string(list_dictionaries):

        """Returns the string representation of a python objects."""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):

        """Returns the python object representation of a json string."""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
