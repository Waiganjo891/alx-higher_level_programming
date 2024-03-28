#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL,
and displays the value of the variable X-Request-Id
in the response header.
"""
import sys
import requests


def get_x_request_id(url):
    """
    Sends a request to the URL and displays the value of
    the variable X-Request-Id in the response header.
    Args:
        url (str): The URL to send the request to.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
