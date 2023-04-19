#!/usr/bin/python3

"""Returns a list of all the attributes of a class."""


def lookup(obj):

    """Gets and returns a list of attributes."""

    attr = dir(obj)
    return attr
