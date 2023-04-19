#!/usr/bin/python3

"""Checks if an object is a instance of or instance of an object"""


def is_kind_of_class(obj, a_class):

    """Checks if obj is an instance of a_class, Return true Else false."""

    if isinstance(obj, a_class) is True:
        return True
    else:
        return False


if __name__ == "__main__":
    a = 10
    print(is_kind_of_class(a, int))
    print(is_kind_of_class(a, float))
    b = True
    print(is_kind_of_class(b, bool))
    print(is_kind_of_class(b, int))
    print(is_kind_of_class(b, object))
