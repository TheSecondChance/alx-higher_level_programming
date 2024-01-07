#!/usr/bin/python3
"""
sends a request to the URL and
displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    tyak = requests.get(sys.argv[1])
    if tyak.status_code >= 400:
        print("Error code: {}".format(tyak.status_code))
    else:
        print(tyak.text)
