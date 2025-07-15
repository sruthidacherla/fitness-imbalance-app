import json
import os

USER_DATA_FILE = "data/users.json"

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return{}

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

def register_users(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True

def check_user(username, password):
    users = load_users()
    return users.get(username) == password