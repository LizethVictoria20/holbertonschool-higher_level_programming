#!/usr/bin/python3
'''2-square.py: Python script that defines square,
   private instantiation attribute of size'''


class Square:
    '''Creates an class Square'''
    def __init__(self, size=0):
        '''Initializes Square with size with zero'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
