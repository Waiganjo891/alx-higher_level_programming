#!/usr/bin/python3
"""
This script takes a URL and an email address as input,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response.
"""
import sys
import requests


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        return
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    if response.status_code == 200:
        print(response.text)
    else:
        print(
            f"Failed to send POST request. Status code:", response.status_code
            )


if __name__ == "__main__":
    main()
