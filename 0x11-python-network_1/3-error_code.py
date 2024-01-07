#!/usr/bin/python3
"""
takes in a URL, sends a request and displays
the body of the response
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            akal = res.read()
            print(akal.decode('utf-8'))
    except error.HTTPError as chegr:
        print('Error code: {}'.format(chegr.code))
