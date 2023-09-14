#!/usr/bin/python3

"""Program to create the base class of the rectangle and
   square objects.
"""


class Base:

    """The base class of the rectangle and square object."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
