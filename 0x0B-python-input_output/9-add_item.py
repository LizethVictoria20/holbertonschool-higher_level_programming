#!/usr/bin/python3
'''[read, write files]
'''
import json
import sys


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

file_name = "add_item.json"

try:
    new = load_from_json_file(file_name) + sys.arvg[1:]

except Exception:
    new = sys.argv[1:]

save_to_json_file(new, file_name)
