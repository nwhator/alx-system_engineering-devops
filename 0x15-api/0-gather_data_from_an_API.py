#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Retrieve TODO list for the given employee ID
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Extract completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    # Display output
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))

    # Display titles of completed tasks
    [print("\t{}".format(task)) for task in completed_tasks]

# Example usage:
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to get and display employee TODO list progress
    get_employee_todo_progress(employee_id)
