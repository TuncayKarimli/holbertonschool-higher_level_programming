#!/usr/bin/python3
"""
This module takes a URL, sends a request, and displays the response body.
It handles urllib.error.HTTPError exceptions to print the status code.
"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
