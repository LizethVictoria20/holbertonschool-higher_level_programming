#!/usr/bin/python3
'''[class Rectangle that defines a rectangle]
'''


class Rectangle:
    '''[defines a rectangle]
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        '''[print __str__]

        Returns:
            [self]
        '''
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height - 1):
                print(str(self.print_symbol) * self.__width)
            return (str(self.print_symbol) * self.__width)
        else:
            return ""

    def __repr__(self):
        '''[__repr__]
        Returns:
            [self]
        '''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        '''[__del__]
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        '''[heigt]
        Args:
            value ([int]): [value from rectangle]
        '''
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
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
        else:
            return 0
