#!/usr/bin/python3
'''102-square.py: Compare 2 squares'''


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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size

        def __lt__(self, other):
            return (self.area() < other.area())

        def __gt__(self, other):
            return (self.area() > other.area())

        def __le__(self, other):
            return (self.area() <= other.area())

        def __ge__(self, other):
            return (self.area() >= other.area())

        def __ne__(self, other):
            return (self.area() != other.area())

        def __eq__(self, other):
            return (self.area() == other.area())
