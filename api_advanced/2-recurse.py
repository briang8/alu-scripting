#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing titles
    of all hot articles for a given subreddit. If the subreddit is invalid,
    returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom_user_agent/0.0.1"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            return None

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("data", {}).get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
