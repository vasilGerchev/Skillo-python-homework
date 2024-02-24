class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed book: {book.title}")
                return
        print("Book not found.")

    def rent_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"Rented book: {book.title}")
                return
        print("Book not available or not found.")

    def archive_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"Archived book: {book.title}")
                return
        print("Book not found.")

# Example usage:
library = Library()

# Adding books
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

# Renting a book
library.rent_book("1984")

# Removing a book
library.remove_book("The Great Gatsby")

library.rent_book("The Great Gatsby")

# Archiving a book
library.archive_book("To Kill a Mockingbird")