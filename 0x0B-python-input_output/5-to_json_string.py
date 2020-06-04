#!/usr/bin/python3
'''[read, write files]
'''


import json


def to_json_string(my_obj):
    '''[to_json_string]

    Args:
        my_obj ([type]): [description]

    Returns:
        [json]: [JSON representation]
    '''
    return json.dumps(my_obj)
