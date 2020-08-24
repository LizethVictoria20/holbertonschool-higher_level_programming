#!/usr/bin/python3
"""POST an email #1"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    url = sys.argv[1]
    email = sys.argv[2]
    new_param = {'email': email}
    value = requests.post(url, data=new_param)
    print(value.text)
