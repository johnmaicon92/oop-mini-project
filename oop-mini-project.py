"""
Enhanced User Interface (UI) and Menu:

Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
    Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit
Book Operations:
        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
User Operations:
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
Author Operations:
        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
Class Structure:
Implement a class structure that represents key entities in the library management system, including:
Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status.
User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
Author: A class representing book authors with attributes like name and biography.


Encapsulation:

Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.


Modules:

Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.


Menu Actions:

Implement the following actions in response to menu selections using the classes you've created:


Adding a new book with all relevant details.
Allowing users to borrow a book, marking it as "Borrowed."
Allowing users to return a book, marking it as "Available."
Searching for a book by its unique identifier (title) and displaying its details.
Displaying a list of all books with their unique identifiers.
Adding a new user with user details.
Viewing user details.
Displaying a list of all users.
Adding a new author with author details.
Viewing author details.
Displaying a list of all authors.
Quitting the application.


User Interaction:

Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
Implement input validation using regular expressions (regex) to ensure the correct formatting of user input. (Bonus)


Error Handling:

Implement error handling where applicable using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.


GitHub Repository:

Create a GitHub repository for your project and commit code regularly.
Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
Include a link to your GitHub repository in your project documentation.


Optional Bonus Points

Text File Handling (Bonus): Implement text file handling to load and save data for various entities in the library management system, such as books, users, authors, and genres. Create dedicated text files for each entity type and develop methods to read data from these files during system startup and save data to them when changes occur. Ensure data integrity and error handling during file operations.
Reservation System (Bonus): Enhance the system by implementing a reservation system. Users can reserve books that are currently unavailable, and the system will notify them when the book becomes available. Develop methods to handle reservations, check availability, and notify users of reservation status changes.
Fine Calculation (Bonus): Implement a fine calculation system for overdue books. Assign due dates to borrowed books, and calculate fines for users who exceed the due date. Develop a mechanism for users to pay fines and update their accounts accordingly.

"""


