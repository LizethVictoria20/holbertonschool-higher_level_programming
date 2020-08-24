#!/usr/bin/python3
"""Response header value #1"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    url = sys.argv[1]
    value = requests.get(url)
    value_header = value.headers.get('x-request-id')
    print(value_header)
