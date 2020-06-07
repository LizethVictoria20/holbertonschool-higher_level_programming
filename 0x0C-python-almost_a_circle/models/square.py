#!/usr/bin/python3
'''[project almost a circle]
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''[Class Square]
    Args:
        Rectangle ([Class]): [description]
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''[__init__]
        '''
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''[__str__]
        '''
        varStr = "[Square] ({}) {}/{} - {}"
        return varStr.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''[size]
        '''
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
