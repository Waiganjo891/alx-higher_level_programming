#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""
import requests


def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status
    and displays the body of the response.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.json()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)


if __name__ == "__main__":
    fetch_status()
