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

    @classmethod
    def save_to_file(cls, list_objs):
        '''[save to file]
        '''
        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))
            with open("{}.json".format(cls.__name__), mode='w') as f:
                f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        '''[from json string]
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
    