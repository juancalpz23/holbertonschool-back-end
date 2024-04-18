#!/usr/bin/python3
"""
REST API
"""

import sys
import requests


def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list of a given employee from the JSONPlaceholder API.
    """
    # Fetch employee data from the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch TODO list of the employee from the API
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Count the number of completed tasks
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Get total number of tasks
    total_tasks = len(todos)

    # Get titles of completed tasks
    completed_titles = [todo['title'] for todo in todos if todo['completed']]

    return employee_name, completed_tasks, total_tasks, completed_titles


def get_employee():
    """
    Main function to execute the script.
    """
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch employee's TODO list
    e_name, c_tasks, t_tasks, c_titles = fetch_employee_todo_list(employee_id)

    # Display TODO list progress
    print(f"Employee {e_name}is done with tasks({c_tasks}/{t_tasks}): ")
    for title in c_titles:
        print(f"    {title}")


if __name__ == "__main__":
    get_employee()
