#!/usr/bin/python3
"""
akes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
