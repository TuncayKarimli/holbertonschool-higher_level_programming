#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /tmp/res -w "%{http_code}" "$1" | grep -q "200" && cat /tmp/res
