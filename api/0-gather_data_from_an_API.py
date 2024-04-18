#!/usr/bin/python3
"""
 0-gather_data_from_an_API
 Given employee ID, returns information
 about his/her todo list progress.
"""
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list of a given employee from the JSONPlaceholder API.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = base_url + f"users/{employee_id}"
    todos_url = base_url + f"todos/?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    if not user_data or not todos_data:
        print("No data found for the given user ID.")
        sys.exit(1)

    return user_data['name'], todos_data


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, todos_data = fetch_employee_todo_list(employee_id)

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{})"
          .format(employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    main()
