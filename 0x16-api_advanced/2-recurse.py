#!/usr/bin/python3
"""Query a array to hot posts for subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns an arrray for all sub all hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    custom_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    spec_params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=custom_headers, params=spec_params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
