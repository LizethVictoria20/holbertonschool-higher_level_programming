#!/usr/bin/python3
'''[project almost a circle]
'''

from models.base import Base


class Rectangle(Base):
    '''[Rectangle inherits from Base]

    Args:
        Base ([class]): [description]
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

        super().__init__(id)

    '''Getter and setter'''
    @property
    def width(self):
        '''[getter]
        '''
        return self.__width

    @property
    def height(self):
        '''[getter]
        '''
        return self.__height

    @property
    def x(self):
        '''[getter]
        '''
        return self.__x

    @property
    def y(self):
        '''[getter]
        '''
        return self.__y

    @width.setter
    def width(self, width):
        '''[setter]
        '''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        '''[setter]
        '''
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        '''[setter]
        '''
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        '''[setter]
        '''
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height
