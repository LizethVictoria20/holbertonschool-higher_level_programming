#!/usr/bin/python3
"""My Github!"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    result = requests.get(url)
    try:
        values = result.json()
        for i in range(10):
            print("{}: {}".format(values[i]["sha"],
                                  values[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
