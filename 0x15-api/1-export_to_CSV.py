#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
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

    # Export to CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create CSV writer
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write header row
        writer.writerow(["User ID", "Username", "Completed", "Title"])

        # Write rows for each task
        [writer.writerow(
		[user_id, username, t.get("completed"), t.get("title")])
		for t in todos]
