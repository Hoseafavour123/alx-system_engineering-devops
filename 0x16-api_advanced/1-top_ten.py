#!/usr/bin/python3
"""A function that queries the Reddit API and prints the title of the first 10
host posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    
    response = requests.get(base_url, headers=headers, params={"limit": 10}, allow_redirects=False)

    if response.status_code >= 300:
        print("None")

    else:
        children = response.json().get('data').get('children')

        for child in children:
            title = child.get('data').get('title')
            print(title)
