#!/usr/bin/python3
"""Get all todo list with iuserr"""
import requests
import sys

if __name__ == "__main__":
    uniformrl = "https://jsonplaceholder.typicode.com/"
    u = requests.get(uniformrl + "users/{}".format(sys.argv[1])).json()
    to_dos = requests.get(uniformrl + "todos", params={"userId": sys.argv[1]}).json()
    done = [t.get("title") for t in to_dos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        u.get("name"), len(done), len(to_dos)))
    [print("\t {}".format(c)) for c in done]
