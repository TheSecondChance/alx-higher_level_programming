#!/usr/bin/python3
"""URL and an email address,
sends a POST request to the passed URL
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)
