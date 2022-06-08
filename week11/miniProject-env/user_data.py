import json
all_users = 'users.json'

def add_user(user):
    with open(all_users, 'w') as file:
        users = json.load(file)
        users.append(user)

def check_user(user):
    with open(all_users, 'r') as file:
        users = json.load(file)
        

