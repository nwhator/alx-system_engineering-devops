#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    # Get employee ID from command-line argument
    user_id = sys.argv[1]

    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract username
    username = user.get("username")

    # Retrieve TODO list for the given employee ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Define JSON file name
    json_file_name = "{}.json".format(user_id)

    # Export to JSON file
    with open(json_file_name, "w") as jsonfile:
        json.dump({
            user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]
        }, jsonfile)
