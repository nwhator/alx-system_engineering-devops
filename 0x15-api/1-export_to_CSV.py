#!/usr/bin/python3
"""Exports employee TODO list progress to CSV."""
import requests
import csv
import sys

def export_to_csv(employee_id):
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Retrieve TODO list for the given employee ID
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Prepare data for CSV
    data = []
    for task in todos:
        task_data = [user.get("id"), user.get("username"), str(task.get("completed")), task.get("title")]
        data.append(task_data)

    # Write data to CSV file
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(data)

# Example usage:
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to export employee TODO progress to CSV
    export_to_csv(employee_id)
