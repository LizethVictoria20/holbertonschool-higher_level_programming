#!/usr/bin/python3
'''[Project about inheritance]
'''


def inherits_from(obj, a_class):
    '''[inherits from]

    Args:
        obj ([int]): [description]
        a_class ([obj]): [description]
    '''
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
        else:
            False
