#!/usr/bin/python3
"""Write a function that Divide a matrix. Returns an integer: Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Arguments:
        matrix {[matrix]} -- [description]
        div {[Div number]} -- [Number to multipli]
    """
    list1 = []
    if type(matrix) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for m in matrix:
        new_list = []
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        else:
            for k in m:
                new_list.append(round((k / div), 2))
            list1.append(new_list)
    return(list1)
