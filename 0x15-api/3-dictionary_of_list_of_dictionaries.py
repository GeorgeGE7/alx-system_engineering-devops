#!/usr/bin/python3
"""get out all todos forr jsonplaceholder api."""
import json
import requests

if __name__ == "__main__":
    uniformrl = "https://jsonplaceholder.typicode.com/"
    u = requests.get(uniformrl + "users").json()
    with open("todo_all_employees.json", "w") as ajfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(uniformrl + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in u}, ajfile)
