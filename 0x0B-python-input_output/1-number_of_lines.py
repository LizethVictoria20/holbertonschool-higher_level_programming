#!/usr/bin/python3
'''[read, write files]
'''


def number_of_lines(filename=""):
    '''[number of lines]

    Args:
        filename (str, optional): [description]. Defaults to "".
    '''
    count = 0
    with open(filename, encoding="utf-8") as f:
        return len(f.readlines())
