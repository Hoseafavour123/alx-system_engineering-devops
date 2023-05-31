#!/usr/bin/python3
"""Gather data from API, export to csv"""
import csv
from sys import argv
import requests


if __name__ == '__main__':
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(argv[1])).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={'userId': argv[1]}).json()

    with open("{}.csv".format(usr.get('id')), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in todos:
            writer.writerow([item.get('userId'), usr.get('username'),
                            item.get('completed'), item.get('title')])
