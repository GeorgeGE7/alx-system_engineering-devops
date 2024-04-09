#!/usr/bin/python3
"""Print all hot posts for one sub"""
import requests


def top_ten(subreddit):
    """Print header for 10 hottest posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    custome_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=custome_headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]
