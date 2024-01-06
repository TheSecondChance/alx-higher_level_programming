#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    valuEmail = {'email': sys.argv[2]}
    data = parse.urlencode(valuEmail)
    data = data.encode('ascii')
    tyak = request.Request(sys.argv[1], data)
    with request.urlopen(tyak) as res:
        akal = res.read()
        print(akal.decode('utf-8'))

