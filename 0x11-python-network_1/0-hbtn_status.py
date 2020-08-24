#!/usr/bin/python3
# What's my status? #0
import urllib.request

if __name__ == "__main__":
    """[Function initial]"""
    req = urllib.request.Request('https://intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        value_h = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(value_h)))
        print('\t- content: {}'.format(value_h))
        print('\t- utf8 content: {}'.format(value_h.decode(unicode='utf-8')))
