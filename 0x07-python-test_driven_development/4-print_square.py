#!/usr/bin/python3
"""Write a function that prints a square with the character #
"""


def print_square(size):
    '''[print_square]

    Args:
        size ([size]): [Length size]

    Raises:
        TypeError: [size must be an integer]
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
