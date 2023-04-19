#!/usr/bin/python3

"""checks if an object is a direct instance of a class."""


def is_same_class(obj, a_class):

    """Checks if obj is an instance of a_class, Return true Else false."""

    if type(obj) == a_class:
        return True
    else:
        return False


if __name__ == "__main__":
    a = 10
    print(is_same_class(a, int))
    print(is_same_class(a, float))
    b = True
    print(is_same_class(b, bool))
    print(is_same_class(b, int))
    print(is_same_class(b, object))
