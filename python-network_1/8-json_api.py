#!/usr/bin/python3
"""
This module sends a POST request to a search API with a letter as a parameter.
It handles JSON response formatting and empty result cases.
"""
import requests
import sys


if __name__ == "__main__":
    # Set q to the first argument, or an empty string if none provided
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}
    # Mandatory firewall bypass header
    headers = {'cfclearance': 'true'}

    try:
        response = requests.post(url, data=payload, headers=headers)
        # Attempt to parse the response as JSON
        json_content = response.json()

        if json_content:
            # Display the result in the format [<id>] <name>
            print("[{}] {}".format(json_content.get('id'),
                                   json_content.get('name')))
        else:
            # JSON is valid but empty
            print("No result")

    except ValueError:
        # Raised if the response body is not valid JSON
        print("Not a valid JSON")
