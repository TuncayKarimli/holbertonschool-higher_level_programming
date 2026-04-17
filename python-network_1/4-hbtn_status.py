#!/usr/bin/python3
"""
This module fetches https://intranet.hbtn.io/status using the requests package.
It displays the type and content of the response body.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    # Mandatory firewall bypass header
    headers = {'cfclearance': 'true'}

    response = requests.get(url, headers=headers)
    
    print("Body response:")
    # Using 4 spaces to match the 'cat -e' example exactly
    print("- type: {}".format(type(response.text)))
    print("- content: {}".format(response.text))
