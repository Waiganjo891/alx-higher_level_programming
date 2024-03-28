#!/usr/bin/python3
"""
Module: github_user_id
"""
import requests
import sys


def get_github_user_id(username, token):
    """
    Function to fetch the GitHub user ID using Basic
    Authentication with a personal access token.
    Args:
        username (str): GitHub username.
        token (str): Personal access token.
    Returns:
        str: GitHub user ID.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, token))
    user_data = response.json()
    return user_data.get('id')


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    github_user_id = get_github_user_id(username, token)
    print("Your GitHub user ID is:", github_user_id)
