#!/usr/bin/python3
'''
    A simple python script since it export data to a json file.
'''

import json
import requests as rq
from sys import argv


def get(url):
    '''Get a data from an REST API resource

    Parameters:
        - url (string): the url of the REST API resource

    Returns:
        - the received data in json format.
    '''
    response = rq.get(url)
    data = response.json()
    return data


def empTodo_json(id):
    '''
        Write the employee TODO list progress of a specific employee
        into a json file.

        Parameters:
            - id (int): id of the employee

        Returns: None
    '''
    base_url = f"https://jsonplaceholder.typicode.com/users/{id}/"
    emp_dt = get(base_url)
    emp_todos = get(base_url + 'todos')
    rows = {id: []}

    for todo in emp_todos:
        row = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': emp_dt['username'],
            }
        rows[id].append(row)

    with open(f"{id}.json", "w", encoding="utf-8") as f:
        json.dump(rows, f)


def main():
    emp_id = argv[1]
    empTodo_json(emp_id)


if __name__ == '__main__':
    main()
