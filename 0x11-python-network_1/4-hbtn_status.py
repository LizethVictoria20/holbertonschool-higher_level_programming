#!/usr/bin/python3
"""What's my status? #0"""
import requests

if __name__ == "__main__":
    """[Function initial]"""

    value = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(value.text)))
    print('\t- content: {}'.format(value.text))
