#!/usr/bin/python3
"""Query subscribers from reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return all subscribers count on sub."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    custom_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=custom_headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get("data")
    return res.get("subscribers")
