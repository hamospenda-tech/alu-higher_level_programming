#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    i = 1
    while i < len(argv):
        total += int(argv[i])
        i += 1
    print(total)
