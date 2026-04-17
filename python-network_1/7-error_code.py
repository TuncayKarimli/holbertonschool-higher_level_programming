#!/usr/bin/python3
"""
This module takes a URL, sends a request using requests, and displays
the response body. If the status code is >= 400, it prints an error.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    # Mandatory firewall bypass header
    headers = {'cfclearance': 'true'}

    response = requests.get(url, headers=headers)

    # Checking if the status code indicates an error (4xx or 5xx)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
