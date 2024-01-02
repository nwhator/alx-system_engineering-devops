#!/usr/bin/python3
"""Exports TODO list progress of all employees to JSON."""
import requests
import json

def export_all_employees_to_json():
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve all users
    users = requests.get(url + "users").json()

    # Prepare data for JSON
    data = {}
    for user in users:
        user_id = str(user.get("id"))
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        tasks_data = [
            {"username": user.get("username"), "task": task.get("title"), "completed": task.get("completed")}
            for task in todos
        ]

        data[user_id] = tasks_data

    # Write data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)  # Adding indent for better readability

# Example usage:
if __name__ == "__main__":
    # Call the function to export TODO progress of all employees to JSON
    export_all_employees_to_json()
