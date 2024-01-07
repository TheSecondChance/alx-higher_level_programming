#!/usr/bin/python3
"""sends a request to the URL and displays"""
import requests
import sys


if __name__ == '__main__':
    akal = requests.get(sys.argv[1])
    print(akal.headers.get('X-Request-Id'))
