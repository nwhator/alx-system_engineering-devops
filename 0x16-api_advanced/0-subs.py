#!/usr/bin/python3
"""
Module to query Reddit API for the number of subscribers in a subreddit.
"""

import requests
from json.decoder import JSONDecodeError


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    Returns:
        int: Number of subscribers. Returns 0 for an invalid subreddit or API error.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # Disable redirects to handle 404 Not Found case
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        # Check if the request was successful or resulted in a 404
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
    except JSONDecodeError:
        # Handle JSON decoding error (response is not in JSON format)
        pass

    # Return 0 for invalid subreddit or API error
    return 0
