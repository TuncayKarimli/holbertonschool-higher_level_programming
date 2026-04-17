#!/usr/bin/python3
"""
This module takes a URL and an email, sends a POST request with the email
as a parameter, and displays the body of the response decoded in utf-8.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data

    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
