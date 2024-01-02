#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Retrieve TODO list for the given employee ID
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Extract completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Display output
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Display titles of completed tasks
    [print("\t {}".format(c)) for c in completed]
