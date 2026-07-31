#!/usr/bin/python3
"""Sends a POST request to a URL with an email and displays the body"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
