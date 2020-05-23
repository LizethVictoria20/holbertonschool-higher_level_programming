#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines
"""


def text_indentation(text):
    '''[Prints a text with 2 new lines]
    Args:
        text ([str]): [text]
    Raises:
        TypeError: [Not found]
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = False
    for i in text:
        if x is False and i == ' ':
                continue
        x = True
        if i in "?:.":
            print("{}\n".format(i))
            x = False
        else:
            print("{}".format(i), end="")
