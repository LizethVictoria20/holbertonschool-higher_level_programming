#!/usr/bin/python3
"""Error code #0"""
import urllib.request
import sys

if __name__ == "__main__":
    """[Function initial]"""
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            value_h = response.read()
            value_h = value_h.decode('utf-8')
            print(value_h)
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
