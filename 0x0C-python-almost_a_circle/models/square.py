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
        return varStr.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        '''[size]
        '''
        return self.width

    @size.setter
    def size(self, size):
        '''[size]
        '''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''[update]
        '''
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value

    def to_dictionary(self):
        '''[to dictionary]
        '''
        s, i, x, y = self.size, self.id, self.x, self.y
        lista = {'size': s, 'id': i, 'x': x, 'y': y}
        return lista
