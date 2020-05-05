#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp = my_list[:]

    if idx < 0:
        return cp
    elif idx >= len(cp):
        return cp
    else:
        cp[idx] = element
        return cp
