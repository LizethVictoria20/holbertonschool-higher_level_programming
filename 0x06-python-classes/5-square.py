#!/usr/bin/python3
'''3-square.py: Python script class Square that defines a square'''


class Square:
    '''Creates class Square type'''

    def __init__(self, size=0):
        '''Initializes Square with size'''
        self.__size = size

    @property
    def size(self):
        '''Define the method to give name'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Access to name and value'''
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size

    def my_print(self):
        '''Print # and depending from size'''
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
