#!/usr/bin/python3
"""get out the todos list using jsonplaceholder api"""
import json
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    uniformrl = "https://jsonplaceholder.typicode.com/"
    u = requests.get(uniformrl + "users/{}".format(u_id)).json()
    u_name = u.get("username")
    to_dos = requests.get(uniformrl + "todos", params={"userId": u_id}).json()
    with open("{}.json".format(u_id), "w") as ajfile:
        json.dump({u_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u_name
            } for t in to_dos]}, ajfile)
