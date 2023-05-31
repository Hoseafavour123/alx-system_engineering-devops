#!/usr/bin/python3
"""Gather data from a REST API.
Obtains the progress of a user in a todo list"""
import requests
from sys import argv


if __name__ == '__main__':
    total = 0
    completed = 0

    usr = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(eval(argv[1])))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    if usr.status_code == 200 and todos.status_code == 200:
        usr = usr.json()
        todos = todos.json()
        for i in range(0, len(todos)):
            if todos[i]['userId'] == eval(argv[1]):
                if todos[i]["completed"] is True:
                    completed += 1
                total += 1

        print("Employee {} is done with tasks({}/{}):"
              .format(usr['name'], completed, total))

        for i in range(0, len(todos)):
            if todos[i]['userId'] == eval(argv[1]) \
                    and todos[i]['completed'] is True:
                print("  {}".format(todos[i]['title']))
