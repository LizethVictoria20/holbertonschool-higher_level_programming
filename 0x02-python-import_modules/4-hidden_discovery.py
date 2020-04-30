#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name_module = dir(hidden_4)
    for i in name_module:
        if not i.startswith('__'):
            print(i)
