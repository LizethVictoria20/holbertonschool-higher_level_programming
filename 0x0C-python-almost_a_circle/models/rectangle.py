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
        '''[area]
        Returns:
            [int]: [description]
        '''
        return self.__width * self.__height

    def display(self):
        '''[display]
        '''
        row = self.height
        column = self.width
        for i in range(self.__y):
            print()
        for j in range(row):
            print(" " * self.__x, end="")
            print("#" * column)

    def __str__(self):
        '''[__str__]
        '''
        varRec = "[Rectangle] ({}) {}/{} - {}/{}"
        return varRec.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''[update]
        '''
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
