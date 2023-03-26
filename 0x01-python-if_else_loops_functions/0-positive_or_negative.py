#!/usr/bin/python3
# program to detect the sign of a number
import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is negative".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is positive".format(number))
