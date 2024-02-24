from book import Book
from reader import Reader


class Library:

    def __init__(self):
        self.books = []
        self.reader = []


    def add_reader(self, name, id_):
        reader = Reader(name, id_)
        self.reader.append(reader)
        return f"Added Reader: {name}"

    def add_book(self, name, book_id, autor):
        book = Book(name, book_id, autor)
        self.books.append(book)
        return f"Added book: {book.name} by {book.autor}"

    def remove_book(self, name, book_id):
        for book in self.books:
            if book.name == name and book.book_id == book_id:
                self.books.remove(book)
                return f"The book {book.name} was removed"
            elif book.name == name or book.book_id == book_id:
                return f"Wrong Name or Book ID"

    def rent_book(self, name, book_id, reader):
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                return f"Rented book: {book.name} is rented from {reader}"
            else:
                return "Book not available or not found"

    def archive_book(self, name, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.is_available = True
                return f"archived book {book.name}"
            else:
                return "Book not available or not found"


Library = Library()

# add reader
added_reader = Library.add_reader("Vasil Gerchev", 98765)
# add book
added_book = Library.add_book("The Great Gatsby", 1234567, "F. Scott Fitzgerald")
print(added_book)

added_book = Library.add_book("To Kill a Mockingbird", 1234568, "Harper Lee")
print(added_book)

added_book = Library.add_book("1984", 1234569, "George Orwell")
print(added_book)

remove_book = Library.remove_book("To Kill a Mockingbird", 1234567, )
print(remove_book)

remove_book = Library.remove_book("To Kill a Mockingbird", 1234568, )
print(remove_book)

archived_book = Library.archive_book("The Great Gatsby", 1234567)
print(archived_book)

archived_book = Library.archive_book("To Kill a Mockingbird", 1234568)
print(archived_book)

rented_book = Library.rent_book("The Great Gatsby", 1234567, "Vasil Gerchev")
print(rented_book)
