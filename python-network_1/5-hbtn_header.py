#!/usr/bin/python3
"""
This module takes a URL, sends a request using requests, and displays
the value of the X-Request-Id variable found in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}

    response = requests.get(url, headers=headers)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
