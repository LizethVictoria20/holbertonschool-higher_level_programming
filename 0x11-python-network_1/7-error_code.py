#!/usr/bin/python3
"""Error code #1"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError as error:
        print("Error code: {}".format(response.status_code))
