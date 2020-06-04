#!/usr/bin/python3
'''[read, write files]
'''


def write_file(filename="", text=""):
    '''[write file]

    Args:
        filename (str, optional): [description]. Defaults to "".
        mode (str, optional): [description]. Defaults to "w".
        text (str, optional): [description]. Defaults to "".
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        new_text = f.write("{}".format(text))
        return new_text
