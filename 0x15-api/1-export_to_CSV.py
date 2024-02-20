#!/usr/bin/python3
"""
Script that, using a REST API, for a given employee ID,
exports data in CSV format.
"""

import csv
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

    # Writing data to CSV file
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([
                employee_id,
                user_info.get('username'),
                task.get('completed'),
                task.get('title')
            ])

    print("CSV file '{}' has been created.".format(filename))
