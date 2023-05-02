#!/usr/bin/python3

"""An empty class."""


class BaseGeometry:

    """implements a dummy geometry method."""

    def area(self):

        """implements nothing."""

        raise Exception("area() is not implemented")


if __name__ == "__main__":
    a = BaseGeometry()
    try:
       print(a.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
