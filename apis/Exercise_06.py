'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

import requests

server_url = "http://www.server.com/data"

# Create functions for the SEVEN options.

def new_account_POST():
    '''
    Takes user info and sends it to the server.

    Takes in users first name, last name and email.

    Creates new entry in database with input.
    '''

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email_address = input("Enter your email: ")

    post_data = {"first_name": first_name, "last_name": last_name, "email": email_address, tasks: ""}

    new_account_post = requests.post(server_url, json=post_data)

    return()



#Create menu for options and take user input.

selection = None

while selection == None:
    print('''Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE))''')

    selection = int(input(":"))

    if selection == 1:
        new_account_POST()
    elif selection == 2:
        view_tasks_GET()
    elif selection == 3:
        view_completed_GET()
    elif selection == 4:
        view_incomplete_GET()
    elif selection == 5:
        view_new_task_POST()
    elif selection == 6:
        update_task_PUT()
    elif selection == 7:
        delete_task_DEL()
    else:
        print("Please enter a selection")
        selection == None
