#!/usr/bin/python3
'''[project almost a circle]
'''
import json


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
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        '''[to json string]
        '''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
