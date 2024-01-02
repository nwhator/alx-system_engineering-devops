#!/usr/bin/python3
"""Exports employee TODO list progress to JSON."""
import requests
import json
import sys


def export_to_json(employee_id):
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Retrieve TODO list for the given employee ID
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Prepare data for JSON
    data = {str(user.get("id")): [{"task": task.get("title"), "completed": task.get("completed"), "username": user.get("username")} for task in todos]}

    # Write data to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)


# Example usage:
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to export employee TODO progress to JSON
    export_to_json(employee_id)
