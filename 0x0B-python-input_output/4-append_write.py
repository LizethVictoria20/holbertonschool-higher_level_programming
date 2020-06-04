#!/usr/bin/python3
'''[read, write files]
'''


def append_write(filename="", text=""):
    '''[append write]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    '''
    new_text = 0
    with open(filename, mode="r", encoding="utf-8") as f:
        new_text += f.write(text)
        return new_text
