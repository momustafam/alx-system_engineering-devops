#!/usr/bin/python3
'''
    A simple python script since it uses a REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''

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


def empTodoProg(id):
    '''Display the employee TODO list progress of a specific employee.

        Parameters:
            - id (int): id of the employee

        Returns: None
    '''
    base_url = f"https://jsonplaceholder.typicode.com/users/{id}/"
    emp_dt = get(base_url)
    emp_todos = get(base_url + 'todos')

    emp_name = emp_dt['name']
    n_todos = len(emp_todos)
    n_comp = 0

    for todo in emp_todos:
        if todo['completed']:
            n_comp += 1
    print(f"Employee {emp_name} is done with tasks({n_comp}/{n_todos}):")
    for todo in emp_todos:
        if todo['completed']:
            print(f'\t {todo["title"]}')


def main():
    emp_id = argv[1]
    empTodoProg(emp_id)


main()
