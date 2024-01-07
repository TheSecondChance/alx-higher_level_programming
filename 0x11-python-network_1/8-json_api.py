#!/usr/bin/python3
"""
http://0.0.0.0:5000/search_user with the letter a parameter
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    qur = sys.argv[1] if len(sys.argv) >= 2 else ""
    mlash = requests.post(url, data={'q': qur})
    try:
        mlashAka = mlash.json()
        if mlashAka:
            print("[{}] {}".format(mlashAka.get('id'), mlashAka.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
