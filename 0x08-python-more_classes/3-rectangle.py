#!/usr/bin/python3
'''[class Rectangle that defines a rectangle]
'''


class Rectangle:
    '''[defines a rectangle]
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        '''[print __str__]

        Returns:
            [self]: [description]
        '''
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__height - 1):
                    print("#" * self.__width)
                return ("#" * self.__width)
        else:
            return ""

    @property
    def width(self):
        '''[width rectangle]
        Returns:
            [int]: [width rectangle]
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''[width]
        Args:
            value ([int]): [value from rectangle]
        '''
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
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
        '''[heigt]
        Args:
            value ([int]): [value from rectangle]
        '''
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''[area rectangle]
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''[perimeter]
        '''
        if self.__width != 0 or self.__height != 0:
            return 2 * (self.__width + self.__height)
        return 0
