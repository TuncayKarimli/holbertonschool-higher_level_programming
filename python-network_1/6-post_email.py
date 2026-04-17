#!/usr/bin/python3
"""
This module takes a URL and an email, sends a POST request with the email
as a parameter using the requests package, and displays the response body.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    headers = {'cfclearance': 'true'}

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
