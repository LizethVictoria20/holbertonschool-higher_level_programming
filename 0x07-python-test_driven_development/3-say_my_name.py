#!/usr/bin/python3
"""Say my name
Write a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """[summary]

    Arguments:
        first_name {[str]} -- [first name]

    Keyword Arguments:
        last_name {str} -- [last name] (default: {""})
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
