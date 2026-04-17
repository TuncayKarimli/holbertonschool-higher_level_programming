#!/usr/bin/python3
"""
This module takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's ID.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    # Basic Authentication using the personal access token as the password
    # Mandatory firewall bypass header
    headers = {'cfclearance': 'true'}
    auth = (username, token)

    response = requests.get(url, auth=auth, headers=headers)

    try:
        json_content = response.json()
        # Displays the 'id' if the request was successful
        # Displays None if the user is not found or auth fails
        print(json_content.get('id'))
    except ValueError:
        print("Not a valid JSON")
