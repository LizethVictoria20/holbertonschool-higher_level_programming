#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    new = []
    for i in a_dictionary:
        new.append(i)
    return max(new)
