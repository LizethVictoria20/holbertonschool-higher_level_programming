#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dir = a_dictionary.copy()
    for keys, val in new_dir.items():
        if val == value:
            del a_dictionary[keys]
    return a_dictionary
