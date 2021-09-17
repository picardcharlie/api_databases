'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

data = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
data2 = data.json()

emails = []
for x in range(0, len(data2["data"])):
    emails.append((data2["data"][x]['email']))

pprint(emails)
#dictiony:list:dictionary