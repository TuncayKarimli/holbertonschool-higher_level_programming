#!/usr/bin/python3
"""
This module fetches https://intranet.hbtn.io/status using the requests package.
It displays the type and content of the response body.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
