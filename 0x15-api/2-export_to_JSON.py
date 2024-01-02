#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

import json
import requests


if __name__ == "__main__":
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve information for all users
    users = requests.get(url + "users").json()

    # Define JSON file name
    json_file_name = "todo_all_employees.json"

    # Export to JSON file
    with open(json_file_name, "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
