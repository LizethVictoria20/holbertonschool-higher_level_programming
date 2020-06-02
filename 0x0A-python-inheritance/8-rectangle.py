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
