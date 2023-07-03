#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)."""

from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
