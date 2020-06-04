#!/usr/bin/python3
'''[read, write files]
'''
import json


def from_json_string(my_str):
    '''[from json string]

    Args:
        my_str ([type]): [description]
    '''
    return json.loads(my_str)
