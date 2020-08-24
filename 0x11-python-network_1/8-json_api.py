#!/usr/bin/python3
"""Search API"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""

    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ''
    url = 'http://0.0.0.0:5000/search_user'
    new_param = {'q': q}
    value = requests.post(url, data=new_param)
    try:
        value_json = value.json()
        if len(value_json) == 0:
            print('No result')
        else:
            print("[{}] {}".format(value_json['id'], value_json['name']))
    except ValueError:
        print('Not a valid JSON')
