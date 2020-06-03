#!/usr/bin/python3
'''[read, write files]
'''


def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, encoding="utf-8") as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
