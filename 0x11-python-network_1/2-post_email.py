#!/usr/bin/python3
"""
This script sends a POST request to a
given URL with an email parameter,
using urllib, and displays the body of
the response decoded in utf-8.
"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified
    URL with the email as a parameter.
    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to be sent as a parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
