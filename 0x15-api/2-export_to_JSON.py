#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
exports data in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetching employee info
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    ).json()

    # Fetching TODO list
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)
    ).json()

    # Formatting data as required
    formatted_data = {employee_id: []}
    for task in todo_list:
        formatted_data[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_info.get('username')
        })

    # Writing data to JSON file
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as file:
        json.dump(formatted_data, file)

    print("JSON file '{}' has been created.".format(filename))
