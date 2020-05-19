#!/usr/bin/python3
'''3-square.py: Python script class Square that defines a square'''


class Square:
    '''Creates class Square type'''

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Initializes Square with size in zero'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size
