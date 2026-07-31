#!/usr/bin/python3
"""Sends a request to a URL and displays the body or the HTTP error code"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
