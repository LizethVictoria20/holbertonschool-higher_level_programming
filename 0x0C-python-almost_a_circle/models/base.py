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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''[to json string]
        '''
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''[save to file]
        '''
        obj = []
        if list_objs is not None:
            for i in list_objs:
                obj.append(cls.to_dictionary(i))
            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write(cls.to_json_string(obj))

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
        obj_list = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_output = cls.from_json_string(f.read())
                for obj in list_output:
                    obj_list.append(cls.create(**obj))
        except Exception:
            pass
        return obj_list
