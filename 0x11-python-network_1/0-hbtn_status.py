#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        f_content = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(f_content)))
        print('\t- content: {}'.format(f_content))
        print('\t- utf8 content: {}'.format(f_content.decode('utf-8')))
