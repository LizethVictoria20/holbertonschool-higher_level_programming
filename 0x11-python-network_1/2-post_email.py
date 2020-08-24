#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys

if __name__ == "__main__":
    """[Function initial]"""
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        value_h = response.read()
        value_h = value_h.decode('utf-8')
        print(value_h)
