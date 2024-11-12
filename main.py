from classes import Book, User, Author
from user_interaction import display_main_menu, display_book_operations, display_user_operations, display_author_operations
from error_handling import validate_input
from error_handling import validate_email
from datetime import datetime
from file_handling import load_books, save_books, load_users, save_users, load_authors, save_authors

def main():
    books = load_books('books.txt')
    users = load_users('users.txt')
    authors = load_authors('authors.txt')
    filename = 'users.txt'
    users, existing_emails, existing_library_ids, existing_usernames = load_users(filename)
    new_authors = []
    new_books = []
    

    save_authors(new_authors, 'authors.txt') 
    save_books(new_books, 'books.txt')
    save_users(users, filename)
    while True:
      
        display_main_menu()
        choice = validate_input("Select an option (1-4): ", r'^[1-4]$')
        
        if choice == '1':
            handle_book_operations(books)
        elif choice == '2':
            handle_user_operations(users, existing_emails, existing_library_ids, existing_usernames)
        elif choice == '3':
            handle_author_operations(authors)
        elif choice == '4':
            save_books(books, 'books.txt')
            save_users(users, 'users.txt')
            save_authors(authors, 'authors.txt')
            print("Exiting the Library Management System.")
            break
    
def handle_book_operations(books):
    while True:
        display_book_operations()
        choice = validate_input("Select an option (1-7): ", r'^[1-7]$')
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            borrow_book(books)  
        elif choice == '3':
            return_book(books)  
        elif choice == '4':
            search_book(books)  
        elif choice == '5':
            list_books(books)  
        elif choice == '6':
            remove_book(books)
        elif choice == '7':
            return

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    pub_date_input = input("Enter publication date (MMDDYYYY): ")
    try:
        publication_date = datetime.strptime(pub_date_input, "%m%d%Y").strftime("%m-%d-%Y")
    except ValueError:
        print("Invalid date format. Please use MMDDYYYY.")
        return
    
    isbn = input("Enter ISBN (International Standard Book Number): ")

    for book in books:
        if book.get_title().lower() == title.lower() and book.get_author().lower() == author.lower():
            print(f"Duplicate book found: '{title}' by {author}. Book not added.")
            return

    book = Book(title=title, author=author, isbn=isbn, genre=genre, publication_date=publication_date)
    books.append(book)
    print(f"Book '{title}' added successfully.")

def list_books(books):
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book)

def borrow_book(books):
    title = input("Enter the title of the book to borrow: ")
    author = input("Enter the author of the book: ")

    for book in books:
        if book.get_title().lower() == title.lower() and book.get_author().lower() == author.lower():
            if book.is_borrowed:
                print(f"The book '{title}' by {author} is currently borrowed and cannot be borrowed again until returned.")
            else:
                book.borrow()  
                print(f"You have borrowed '{title}' by {author}.")
            return

    print(f"No book found matching '{title}' by {author}.")

def return_book(books):
    title = input("Enter the title of the book to return: ")
    author = input("Enter the author of the book: ")

    for book in books:
        if book.get_title().lower() == title.lower() and book.get_author().lower() == author.lower():
            if not book.is_borrowed:
                print(f"The book '{title}' by {author} was not borrowed.")
            else:
                book.return_book()  
                print(f"You have returned '{title}' by {author}.")
            return

    print(f"No book found matching '{title}' by {author}.")

def search_book(books):
    title_input = input("Enter the title of the book to search for: ")
    found_books = [book for book in books if title_input.lower() in book.get_title().lower()]

    if found_books:
        print(f"Books found matching '{title_input}':")
        for book in found_books:
            print(book)  
    else:
        print(f"No books found matching '{title_input}'.")

def remove_book(books):
    title = input("Enter the title of the book to remove: ")
    author = input("Enter the author of the book: ")

    for book in books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            books.remove(book)
            print(f"Book '{title}' by {author} has been removed.")
            return

    print(f"No book found matching '{title}' by {author}.")


def handle_user_operations(users, existing_emails, existing_library_ids, existing_usernames):
    while True:
        display_user_operations()
        choice = validate_input("Select an option (1-5): ", r'^[1-5]$')
        
        if choice == '1':
            add_user(users, existing_emails, existing_library_ids, existing_usernames)
        elif choice == '2':
            list_users(users)
        elif choice == '3':
            display_all_users(users)
        elif choice == '4':
            remove_user(users)
        elif choice == '5':
            return

def display_all_users(users):
    if not users:
        print("No users found.")
        return

    print("List of Users:")
    print(f"{'Name':<20} {'Library ID':<15} {'Email':<30} {'Borrowed Books'}")
    print("-" * 80)

    for user in users:
        borrowed_books = ', '.join(user.get_borrowed_books()) if user.get_borrowed_books() else "None"
        print(f"{user.get_name():<20} {user.get_library_id():<15} {user.get_email():<30} {borrowed_books}")

def add_user(users, existing_emails, existing_library_ids, existing_usernames):
    name = input("Enter user name: ").title()
    library_id = input("Enter library ID: ")
    email = input("Enter user email: ")

    if name in existing_usernames:
        print(f"Error: A user with the name '{name}' already exists.")
        return
    if email in existing_emails:
        print(f"Error: A user with the email '{email}' already exists.")
        return
    if library_id in existing_library_ids:
        print(f"Error: A user with the library ID '{library_id}' already exists.")
        return

    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return

    user = User(name, library_id, email)
    users.append(user)
    existing_emails.add(email)
    existing_library_ids.add(library_id)
    existing_usernames.add(name) 
    print(f"User  '{name}' added successfully.")

def list_users(users):
    if not users:
        print("No users available.")
    else:
        for user in users:
            print(user)

def remove_user(users):
    library_id = input("Enter the library ID of the user to remove: ")

    for user in users:
        if user.get_library_id() == library_id:
            users.remove(user)
            print(f"User  with Library ID '{library_id}' has been removed.")
            return

    print(f"No user found with Library ID '{library_id}'.")


def handle_author_operations(authors):
    while True:
        display_author_operations()
        choice = validate_input("Select an option (1-4): ", r'^[1-4]$')
        
        if choice == '1':
            add_author(authors)
        elif choice == '2':
            list_authors(authors)
        elif choice == '3':
            remove_author(authors)
        elif choice == '4':
            return

def add_author(authors):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    author = Author(name=name, biography=biography)
    authors.append(author)
    print(f"Author '{name}' added successfully.")

def list_authors(authors):
    if not authors:
        print("No authors available.")
    else:
        for author in authors:
            print(author)

def remove_author(authors):
    name = input("Enter the name of the author to remove: ")

    for author in authors:
        if author.get_name().lower() == name.lower():
            authors.remove(author)
            print(f"Author '{name}' has been removed.")
            return

    print(f"No author found with the name '{name}'.")


if __name__ == "__main__":
    main()