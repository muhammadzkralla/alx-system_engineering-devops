#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    # Fetching employee info
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id)).json()

    # Fetching TODO list
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                             .format(employee_id)).json()

    total_tasks = len(todo_list)
    done_tasks = [task for task in todo_list if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_info.get('name'), len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
