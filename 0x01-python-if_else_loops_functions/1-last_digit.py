#!/usr/bin/python3
# program to print out the last digit of a number and its sign
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = number % -10
if last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and is not 0".format(number, last_digit))
elif last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
else:
    print("Last_digit of {} is {} and is 0".format(number, last_digit))
