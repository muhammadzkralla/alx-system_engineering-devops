#!/usr/bin/python3
"""
Reddit subs
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API.
    If not a valid subreddit, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)

    # Check if the subreddit exists
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0


# Test the function
if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))
