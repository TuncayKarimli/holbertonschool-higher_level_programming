#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    # Adding the firewall bypass header as per project requirements
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        # Using 4 spaces to match the example's indentation exactly
        print("    - type: {}".format(type(content)))
        print("    - content: {}".format(content))
        print("    - utf8 content: {}".format(content.decode('utf-8')))
