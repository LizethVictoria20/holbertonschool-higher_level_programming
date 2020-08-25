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
        d = result.json()
        for i in range(10):
            print("{}: {}".format(d[i]["sha"],
                                  d[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
