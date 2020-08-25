#!/usr/bin/python3
"""My Github!"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    value_param = {'login': sys.argv[1]}
    request = requests.get(url, params=value_param, auth=(username, password))

    value_json = request.json()
    print(value_json)
    try:
        print(value_json['id'])
    except KeyError:
        print('None')
