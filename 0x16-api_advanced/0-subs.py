#!/usr/bin/python3
"""
Module to query Reddit API for the number of subscribers in a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    Returns:
        int: Number of subscribers. Returns 0 for an invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditScraper/1.0'}
    
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
