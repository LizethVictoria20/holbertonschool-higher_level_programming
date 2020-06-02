#!/usr/bin/python3
'''[Project about inheritance]
'''


def is_same_class(obj, a_class):
    '''[is same class]

    Args:
        obj ([int]): [description]
        a_class ([int]): [description]
    '''
    return issubclass(a_class, type(obj))
