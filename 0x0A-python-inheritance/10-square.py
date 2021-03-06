#!/usr/bin/python3
'''[Project about inheritance]
'''


class BaseGeometry:
    '''[class Geometry module]
    '''
    def area(self):
        '''[function area]
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''[class Rectangle that inherits from BaseGeometry]

    Args:
        BaseGeometry ([class]): [description]
    '''
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        '''[__repr__]
        Returns:
            [self]
        '''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    '''[Square]

    Args:
        Rectangle ([class]): [description]
    '''
    def __init__(self, size):
        '''[__init__]

        Args:
            size ([int]): [description]
        '''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''[area]

        Returns:
            [square]: [description]
        '''
        return self.__size ** 2
