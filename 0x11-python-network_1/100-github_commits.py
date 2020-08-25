#!/usr/bin/python3
"""My Github!"""
import requests
import sys

if __name__ == "__main__":
    """[Function initial]"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    result = requests.get(url)
    try:
        d = result.json()
        for i in range(10):
            sha = d[0]["sha"]
            print("{}: {}".format(sha, d[1]["commit"]["author"]["name"]))
    except KeyError:
        pass
