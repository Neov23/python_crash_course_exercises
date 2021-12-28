# Άσκηση 10-13

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def identify():
    username = get_stored_username()
    try:
        if username:
            answer = input(f"Are you '{username}'? ")
            answer = answer.lower()

            if answer == 'no':
                get_new_username()
            elif answer != 'yes' and answer != 'no':
                identify()

    except NameError:
        print("No username saved.")

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

identify()
greet_user()
