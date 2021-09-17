'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 426 ,
    "first_name": "[Charlie]",
    "last_name": "[Picard]",
    "email": "[pacardcharlee@gmail.com]"
}

put_req = requests.put(base_url, json=body)

get_resp = requests.get(base_url)
print(get_resp.content)