#!/usr/bin/python3
'''3-square.py: Python script class Square that defines a square'''


class Square:
    '''Creates class Square type'''
    def __init__(self, size=0):
        '''Initializes Square with size in zero'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size
