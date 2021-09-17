'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

del_request = requests.delete(base_url + "/426")

print(requests.get(base_url))