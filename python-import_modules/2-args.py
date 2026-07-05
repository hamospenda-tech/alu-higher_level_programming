#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(count))
        i = 1
        while i <= count:
            print("{}: {}".format(i, argv[i]))
            i += 1
