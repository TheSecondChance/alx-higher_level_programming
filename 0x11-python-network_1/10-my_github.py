#!/usr/bin/python3
"""
GitHub credentials
and uses the GitHub API to display user id
"""
import sys
from requests import get, auth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    res = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(res.json().get('id'))
