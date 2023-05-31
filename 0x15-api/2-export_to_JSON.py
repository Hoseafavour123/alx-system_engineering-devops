#!/usr/bin/python3
"""Gather data from API and export to JSON"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    usr = \
          requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(argv[1])).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": argv[1]}).json()
    data = {}
    data["{}".format(argv[1])] = []

    for todo in todos:
        data[argv[1]].append({
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': usr.get('username')})

    with open("{}.json".format(argv[1]), "w") as filename:
        json.dump(data, filename)
