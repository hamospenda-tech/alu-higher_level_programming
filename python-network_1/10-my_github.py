#!/usr/bin/python3
"""Uses the GitHub API to display a user's id via Basic Authentication"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get("https://api.github.com/user",
                       auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get("id"))
