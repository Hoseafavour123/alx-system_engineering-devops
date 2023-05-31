#!/usr/bin/python3
"""Retrieve API data for all todos of all employers"""
import requests
import json


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    empl_data = {}

    for user in users:
        todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=({'userId': user.get('id')})).json()
        empl_data[user.get('id')] = []

        for todo in todos:
            empl_data[user.get('id')].append({
                'username': user.get('username'),
                'task': todo.get('title'),
                'completed': todo.get('completed')})

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(empl_data, jsonfile)
