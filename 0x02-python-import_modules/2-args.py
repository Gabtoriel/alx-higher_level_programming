#!/usr/bin/python3
from sys import argv
def main():
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("{} argument:".format(count), end="\n")
        print("{}: {}".format(count, argv[1]))
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, argv[i + 1]), end="\n")

if __name__ == "__main__":main()
