# library_system.py

class Book:
    """Base class representing a generic book."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f" Book:'{self.title}' by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"E-Book: '{self.title}' by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"Print Book: '{self.title}' by {self.author}, Pages: {self.page_count}"


class Library:
    """Class representing a collection of books (composition)."""

    def __init__(self):
        self.books = []  # list to store Book, EBook, PrintBook

    def add_book(self, book: Book):
        """Add a book instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library has no books yet.")
        else:
            print("Library Collection:")
            for book in self.books:
                print(f" - {book}")
