#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints an error message.
"""
import requests
import sys


def fetch_url_body(url):
    """
    Fetches the body of the response
    from the given URL.
    Args:
        url (str): The URL to send the request to.
    Returns:
        str: The body of the HTTP response.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
        return None
    return response.text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    body = fetch_url_body(url)
    if body:
        print(body)
