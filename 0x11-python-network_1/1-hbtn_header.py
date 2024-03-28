#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys


def get_request_id(url):
    """
    Fetches the value of the X-Request-Id variable
    from the header of the response.
    Args:
        url (str): The URL to send the request to.
    Returns:
        str: The value of the X-Request-Id variable.
    """
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        return request_id


if __name__ == "__main__":
    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)
