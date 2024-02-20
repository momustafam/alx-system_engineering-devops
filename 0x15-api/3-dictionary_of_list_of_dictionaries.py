#!/usr/bin/python3
'''
    A simple python script since it export data to a json file.
'''

import json
import requests as rq


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


def empsTodo_json():
    '''
        Write the employee TODO list progress of all employees
        into a json file.

        Parameters:
            - id (int): id of the employee

        Returns: None
    '''
    base_url = f"https://jsonplaceholder.typicode.com/users/"
    emp_dt = get(base_url)

    rows = {}
    for emp in emp_dt:
        emp_todos = get(base_url + f'{emp["id"]}/' + 'todos')
        rows[emp["id"]] = []
        for todo in emp_todos:
            row = {
                    'username': emp['username'],
                    'task': todo['title'],
                    'completed': todo['completed'],
                }
            rows[emp["id"]].append(row)

    with open("todo_all.json", "w", encoding="utf-8") as f:
        json.dump(rows, f)


def main():
    empsTodo_json()


if __name__ == '__main__':
    main()
