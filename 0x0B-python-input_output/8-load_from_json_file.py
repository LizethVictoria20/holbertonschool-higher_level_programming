#!/usr/bin/python3
'''[read, write files]
'''
import json


def load_from_json_file(filename):
    '''[load from json file]

    Args:
        filename ([type]): [description]
    '''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
