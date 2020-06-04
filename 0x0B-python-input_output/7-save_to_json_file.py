#!/usr/bin/python3
'''[read, write files]
'''
import json


def save_to_json_file(my_obj, filename):
    '''[save to json file]

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
