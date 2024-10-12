class Book:
  "Represents a book in the library."

  def __init__(self, title, author):
    "Initializes a Book object with title, author, and availability."
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def __str__(self):
    "Defines how a Book object is printed."
    return f"{self.title} by {self.author}"


class Library:
  "Manages a collection of Book objects."

  def __init__(self):
    "Initializes a Library object with an empty list of books."
    self._books = []

  def add_book(self, book):
    "Adds a Book object to the library's collection."
    self._books.append(book)

  def check_out_book(self, title):
    "Attempts to check out a book by title, marking it unavailable."
    for book in self._books:
      if book.title == title and not book._is_checked_out:
        book._is_checked_out = True
        print(f"Successfully checked out '{title}'.")
        return
    print(f"Sorry, '{title}' is not available for checkout.")

  def return_book(self, title):
    "Attempts to return a book by title, marking it available."
    for book in self._books:
      if book.title == title and book._is_checked_out:
        book._is_checked_out = False
        print(f"Successfully returned '{title}'.")
        return
    print(f"Sorry, '{title}' is not currently checked out.")

  def list_available_books(self):
    "Prints a list of all available books in the library."
    print("Available books:")
    for book in self._books:
      if not book._is_checked_out:
        print(book)