#!/usr/bin/python3
"""Recursively search for the hottest topics in Reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"count": count, "after": after}

    sub_info = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_lst = hot_list + [child.get('data').get('title') for child in
                          sub_info.json().get('data').get('children')]

    info = sub_info.json()
    if not info.get('data').get('after'):
        return hot_lst

    return recurse(subreddit, hot_l, info.get('data').get('count'),
                   info.get('data').get('after'))
