#!/usr/bin/python3
'''[class Rectangle that defines a rectangle]
'''


class Rectangle:
    '''[defines a rectangle]
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''[width rectangle]
        Returns:
            [int]: [width rectangle]
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''[widt]
        Args:
            value ([int]): [value from rectangle]
        '''
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''[height rectangle]
        Returns:
            [int]: [height rectangle]
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''[widt]
        Args:
            value ([int]): [value from rectangle]
        '''
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")