#!/usr/bin/python3
'''[Project about inheritance]
'''


def inherits_from(obj, a_class):
    '''[inherits from]

    Args:
        obj ([int]): [description]
        a_class ([obj]): [description]
    '''
    if issubclass(a_class, type(obj)):
        return False
    else:
        return True
