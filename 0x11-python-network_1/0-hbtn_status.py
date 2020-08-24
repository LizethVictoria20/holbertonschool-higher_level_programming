#!/usr/bin/python3
# What's my status? #0
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        value_headers = response.read()
        print('Body response:')
        print('\t - type: {}'.format(type(value_headers)))
        print('\t - content: {}'.format(value_headers))
        print('\t - utf8 content: {}'.format(value_headers.decode('utf-8')))
