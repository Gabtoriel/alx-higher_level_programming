#!/usr/bin/python3

"""Checks if a given object is subclass(inherits) of another object."""


def inherits_from(obj, a_class):

    """Checks if obj inherits from a class (a_class."""

    if issubclass(obj, a_class) is True:
        return True
    else:
        return False
