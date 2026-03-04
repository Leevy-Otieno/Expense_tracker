import json
import hashlib
from models.user import Founder, Accountant, Investor

users_file = "data/users.json"

def hash_password(password):
   return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    
    try:
        with open(users_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_users(users):
    """
    Saves the entire user list
    back into the JSON file.
    """
    with open(users_file, "w") as file:
        json.dump(users, file, indent=4)
                
def register():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (founder/accountant/investor): ").lower()

    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            return None

    if role not in ["founder", "accountant", "investor"]:
        print("Invalid role selected.")
        return None

    hashed_password = hash_password(password)

    new_user = {
        "username": username,
        "password": hashed_password,
        "role": role
    }

    users.append(new_user)

    save_users(users)

    print("Registration successful!")
    return None

def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_password:
            print("Login successful!")

            if user["role"] == "founder":
                return Founder(username, hashed_password)
            elif user["role"] == "accountant":
                return Accountant(username, hashed_password)
            elif user["role"] == "investor":
                return Investor(username, hashed_password)

    print("Invalid username or password.")
    return None