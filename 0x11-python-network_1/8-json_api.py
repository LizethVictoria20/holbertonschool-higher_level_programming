#!/usr/bin/python3
"""Search API"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    q = ''
    if len(q) > 1:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    new_param = {'q': q}
    value = requests.post(url, data=new_param)
    try:
        value_json = value.json()
        if value_json:
            print("[{}] {}".format(value_json['id'], value_json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
