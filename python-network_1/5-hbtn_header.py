#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header value"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
