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
        if list_dictionaries is None or len(list_dictionaries) < 0:
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
            Str = "{}.json".format(cls.__name__),
            with open(Str, mode='w', encoding='utf-8') as f:
                f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        '''[from json string]
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''[create]
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Class Method that returns a list of instances'''
        new_list = []
        try:
            varStr = "{}.json".format(cls.__name__)
            with open(varStr, mode='r') as f:
                new = cls.from_json_string(f.read())
        except IOError:
            return []

        for i in new:
            new_list.append(cls.create(**i))
        return new_list
