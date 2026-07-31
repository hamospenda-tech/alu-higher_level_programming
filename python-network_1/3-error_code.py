#!/usr/bin/python3
"""Sends a request to a URL and displays the body or the HTTP error code"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
