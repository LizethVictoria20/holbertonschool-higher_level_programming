#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        count = my_list[0]
        if my_list[i] > count:
            count = my_list[i]
            return count
