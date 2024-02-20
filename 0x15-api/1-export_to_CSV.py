#!/usr/bin/python3
'''
    A simple python script since it export data in the CSV format.
'''

import csv
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


def empTodo_csv(id):
    '''Write the employee TODO list progress of a specific employee into a csv file.

        Parameters:
            - id (int): id of the employee

        Returns: None
    '''
    base_url = f"https://jsonplaceholder.typicode.com/users/{id}/"
    emp_dt = get(base_url)
    emp_todos = get(base_url + 'todos')
    rows = []

    for todo in emp_todos:
        row = [emp_dt['id'], emp_dt['username'], todo['completed'], todo['title']]
        rows.append(row)

    with open("USER_ID.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
        

def main():
    emp_id = argv[1]
    empTodo_csv(emp_id)


if __name__ == '__main__':
    main()
