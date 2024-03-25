#!/usr/bin/python3
"""get csvfiel with jsonplaceholder api"""
import sys
import requests
import csv

if __name__ == "__main__":
    u_id = sys.argv[1]
    uniformrl = "https://jsonplaceholder.typicode.com/"
    u = requests.get(uniformrl + "users/{}".format(u_id)).json()
    u_name = u.get("username")
    to_dos = requests.get(uniformrl + "todos", params={"userId": u_id}).json()
    with open("{}.csv".format(u_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [u_id, u_name, t.get("completed"), t.get("title")]
         ) for t in to_dos]
