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
