Application Features:

Main Menu: When you run the program, you'll see the main menu with the following options:

Book Operations: Manage books in the library.
User Operations: Manage users who can borrow books.
Author Operations: Manage the authors of books.
Exit: Quit the program.

Book Operations:
Add Book: Enter details for a new book (title, author, ISBN, genre, publication date).
Borrow Book: Borrow a book by entering its title and author.
Return Book: Return a book by entering its title and author.
Search Book: Find books by entering a title.
List Books: View all books in the library.
Remove Book: Delete a book from the library.

User Operations:
Add User: Create a new user account with a name, library ID, and email.
List Users: View a list of all users.
Display All Users: View a detailed list of users, including their borrowed books.
Remove User: Delete a user account.
Author Operations:

Add Author: Create a new author entry with a name and biography.
List Authors: View a list of all authors.
Remove Author: Delete an author entry.

The application saves data to text files (books.txt, users.txt, authors.txt).
When you run the program again, it loads data from these files, so your changes are preserved.

The validate_input function helps ensure you enter valid data for certain fields (e.g., numbers, dates).
The validate_email function checks if the entered email address is in a valid format.


Example:

Add a book:
Select option 1 (Book Operations).
Select option 1 (Add Book).
Enter details like title, author, ISBN, genre, and publication date.
Borrow a book:
Select option 1 (Book Operations).
Select option 2 (Borrow Book).
Enter the title and author of the book you want to borrow.
Add a user:
Select option 2 (User Operations).
Select option 1 (Add User).
Enter the user's name, library ID, and email.

If you run the application multiple times, your data will persist in the text files.
The system is not yet very sophisticated, but it provides a foundation for building a more complex library management system.
