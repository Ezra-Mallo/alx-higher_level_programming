#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request to
	http://0.0.0.0:5000/search_user with the letter as a parameter.

    *	The letter must be sent in the variable q
    *	If no argument is given, set q=""
    *	If the response body is properly JSON formatted and not empty, display
    	the id and name like this: [<id>] <name>
	
	Otherwise:
    *	Display Not a valid JSON if the JSON is invalid
    *	Display No result if the JSON is empty
    *	You must use the package requests and sys
    *	You are not allowed to import packages other than requests and sys
    *	Please test your script in the sandbox provided, using the web server
    	running on port 5000. All JSON generated by this server are random.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    my_letter = "" if len(argv) == 1 else argv[1]
    value = {"q": my_letter}
    r = requests.post(url, data=value)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
