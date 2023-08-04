#!/usr/bin/python3

"""Program to print the name of someone."""


def say_my_name(first_name, last_name=""):

    """This function prints a name in a reasonable sentence."""

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))


if __name__ == '__main__':
    say_my_name('victor', 'scott')
    say_my_name('', 'cleric')
    say_my_name('glofffin')
    try:
        say_my_name(True, 'v')
    except Exception as e:
        print(e)
    try:
        say_my_name('vix', [5])
    except Exception as e:
        print(e)
