#!/usr/bin/python3
"""
This module fetches a specific URL using the urllib package.
It displays the type, content, and utf-8 decoded value of the response.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("    - type: {}".format(type(content)))
        print("    - content: {}".format(content))
        print("    - utf8 content: {}".format(content.decode('utf-8')))
