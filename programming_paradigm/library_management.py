class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library(Book):
    def __init__(self, title="library", author="unknown"):
        super().__init__(title, author)
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                print(f"'{book.title}' has been checked out.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                print(f"'{book.title}' has been returned.")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}"
                           for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for b in available_books:
                print(f" - {b}")
        else:
            print("No books are currently available.")

        