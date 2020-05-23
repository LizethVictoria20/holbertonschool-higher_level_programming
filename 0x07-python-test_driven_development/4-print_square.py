#!/usr/bin/python3
"""Write a function that prints a square with the character #
"""


def print_square(size):
    """Print square
    Arguments:
        size {[int]} --  is the size length of the square
    """
    if type(size) is not int and type(size):
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            mul = '#' * size
            print(mul)
