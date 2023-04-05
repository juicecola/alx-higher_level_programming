#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status

import requests

if __name__ == "__main__":
    k = requests.get('https://intranet.hbtn.io/status')
    l = k.text
    print('Body response:\n\t type: {}\n\t- content: {}'.format(type(l), l))
