#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request to the passed
   URL with the email as a parameter, and displays the body of the response
   (decoded in utf-8)"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":

    count = len(argv)
    if count == 3:
        url = argv[1]
        email = argv[2]
        values = {'email': email}

        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(response.read().decode("utf-8"))
