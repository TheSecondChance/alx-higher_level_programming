#!/usr/bin/python3
"""the value of the X-Request-Id variable found in the header of response
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        ht_mez = res.info()
        print(ht_mez.get('X-Request-Id'))
