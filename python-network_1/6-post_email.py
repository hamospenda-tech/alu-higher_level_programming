#!/usr/bin/python3
"""Sends a POST request to a URL with an email and displays the body"""
import requests
import sys


if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(res.text)
