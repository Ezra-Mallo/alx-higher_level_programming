#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)."""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    result = r.headers.get("X-Request-Id")
    print(result)
