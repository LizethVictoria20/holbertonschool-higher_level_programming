#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys

if __name__ == "__main__":
    """[Function initial]"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        value_h = response.headers['x-request-id']
        print(value_h)
