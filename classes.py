class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.is_borrowed = False  

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Genre: {self.genre}\n"
                f"Published: {self.publication_date}\n"
                f"ISBN: {self.isbn}\n"
                f"{'Status: Borrowed' if self.is_borrowed else 'Status: Available'}".title())

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class User:
    def __init__(self, name, library_id, email):
        self.__name = name
        self.__library_id = library_id
        self.__email = email
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id
    
    def get_email(self):
        return self.__email 

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def get_borrowed_books(self):
        return self.__borrowed_books

    def __str__(self):
        borrowed_books_list = ', '.join(self.__borrowed_books) if self.__borrowed_books else "None"
        return f":User  {self.__name}, Library ID: {self.__library_id}, Email: {self.__email}, Borrowed Books: [{borrowed_books_list}]"


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def __str__(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"
    
