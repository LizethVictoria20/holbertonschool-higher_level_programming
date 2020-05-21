#!/usr/bin/python3
"""Write a function that adds 2 integers
a and b must be integers or floats, otherwise raise a TypeError exception
Returns an integer: the addition of a and b
"""
def add_integer(a, b=98):
    """[Function add integer]
        Return the add between a and b 
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)

    return a + b