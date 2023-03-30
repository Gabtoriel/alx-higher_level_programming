#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add
    a = 1
    b = 2
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
