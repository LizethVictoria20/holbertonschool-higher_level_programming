#!/usr/bin/python3
'''3-square.py: Python script class Square that defines a square'''


class Square:
    '''Creates class Square type'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes Square with size and position'''
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        '''Define the method to give name'''
        return self.__position

    @property
    def size(self):
        '''Define the method to give name'''
        return self.__size

    @position.setter
    def position(self, value):
        '''Access to name and value'''
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        '''Access to name and value'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size

    def my_print(self):
        '''Print # and depending from size'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
