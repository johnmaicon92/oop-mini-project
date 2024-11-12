import os
import re
from classes import Book, User, Author

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def save_users(users, filename):
    try:
        with open(filename, 'w') as file:
            for user in users:
                borrowed_books = ';'.join(user.get_borrowed_books())  
                file.write(f"{user.get_name()},{user.get_library_id()},{user.get_email()},{borrowed_books}\n")
    except Exception as e:
        print(f"Error saving users: {e}")

def load_users(filename):
    users = []
    existing_emails = set()
    existing_library_ids = set()
    
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    name, library_id, email, borrowed_books = line.strip().split(',')
                    user = User(name, library_id, email)  
                    user.borrowed_books = borrowed_books.split(';') if borrowed_books else []
                    users.append(user)
                    existing_emails.add(email)
                    existing_library_ids.add(library_id)
    except Exception as e:
        print(f"Error loading users: {e}")
    
    return users, existing_emails, existing_library_ids


def add_user(users):
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    email = input("Enter user email: ")
    
    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return

    user = User(name, library_id, email)
    users.append(user)
    print(f"User  '{name}' added successfully.")