class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        self._title = title
        self._author = author
        self._publication_year = publication_year

    def __del__(self):
        print(f"Deleting {self._title}")

    def __str__(self) -> str:
        return f"{self._title} by {self._author}, published in {self._publication_year}"

    def __repr__(self):
        return f"Book({self._title}, {self._author}, {self._publication_year})" 
       
    
        