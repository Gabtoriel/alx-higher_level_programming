#!/usr/bin/python3

"""Checks if a given object is subclass(inherits) of another object."""


def inherits_from(obj, a_class):

    """Checks if obj is a subclass of another class."""

    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False


if __name__ == "__main__":
    a = True
    print(inherits_from(a, int))
    print(inherits_from(a, bool))
    print(inherits_from(a, object))
