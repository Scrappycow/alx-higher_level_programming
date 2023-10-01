#!/usr/bin/python3
"""
Takes a URL & email, sends POST request to passed URL with email as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
