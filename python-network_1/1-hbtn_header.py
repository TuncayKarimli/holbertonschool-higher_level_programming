#!/usr/bin/python3
"""
This module takes a URL as an argument, sends a request, and displays
the value of the X-Request-Id variable found in the response header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    # Applying the mandatory firewall bypass header
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        # Using .get() as requested to safely access the header
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
