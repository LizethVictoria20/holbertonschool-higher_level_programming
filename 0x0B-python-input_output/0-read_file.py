#!/usr/bin/python3
'''[read, write files]
'''


def read_file(filename=""):
    '''[read_file]

    Args:
        filename (str, file): [description]. Defaults to "".
    '''
    with open("my_file_0.txt", encoding="utf-8") as File:
        print(File.read())
