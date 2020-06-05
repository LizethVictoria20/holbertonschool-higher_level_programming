#!/usr/bin/python3
'''[project almost a circle]
'''


class Base:
    '''[Class Base]
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''[__init__]

        Args:
            id ([int], optional): [description]. Defaults to None.
        '''
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
