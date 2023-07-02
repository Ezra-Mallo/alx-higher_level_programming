#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    my_req = Request(url)
    with urlopen(my_req) as respons:
        content = response.read()

    print("Body response:")
    print("\t- type: {}".format{type(content)}
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}",format(content.decode('utf-8')))
