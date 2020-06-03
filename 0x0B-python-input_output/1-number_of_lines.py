#!/usr/bin/python3
'''[read, write files]
'''


def number_of_lines(filename=""):
    count = 0
    with open("my_file_0.txt", encoding="utf-8") as File:

        for line in File:
            count += 1
        return count
