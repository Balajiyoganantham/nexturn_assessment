
# Scenario Overview:
# You are tasked with developing a Library Management System for a medium-sized library. The system should be able to manage Books, Members, and their borrowing activities. The focus of the case study is on applying Object-Oriented Programming (OOP) principles like encapsulation, inheritance, and polymorphism, along with effective use of Exception Handling (both built-in and user-defined exceptions).

# The system should allow members to borrow and return books while keeping track of the availability of books in the library. Additionally, the system must restrict the number of books a member can borrow simultaneously, which will require custom exception handling.

# Functional Requirements:
# Books:

# Each book should have a unique ID, a title, an author, and a status indicating if it is available or borrowed.
# The system should allow new books to be added to the library's collection.
# Books should be categorized as fiction or non-fiction.
# Members:

# Members should have a unique ID, a name, and a record of the books they have borrowed.
# There should be two types of members: Regular and Premium. Regular members can borrow up to 3 books at a time, while Premium members can borrow up to 5 books.
# Members should have methods to borrow and return books, and the system should update the status of the book accordingly.
# Library:

# The library should maintain a collection of books and handle book lending and returns.
# The library should keep track of which books are currently available and which are borrowed.
# Borrow and Return System:

# A member can borrow a book if it is available.
# When a book is borrowed, its availability status must be updated, and the borrowing must be recorded in the member’s profile.
# When a book is returned, the status must be updated, and the record should be removed from the member’s profile.
# Non-Functional Requirements:
# Exception Handling:

# The system must handle cases where a member tries to borrow a book that is already borrowed.
# The system must also handle scenarios where a member tries to borrow more books than they are allowed (Regular or Premium).
# Use both built-in exceptions (e.g., ValueError, IndexError) and create a user-defined exception for when a member exceeds their borrowing limit.
# Scalability:

# The system should be designed to handle an expanding list of members and books, and manage borrowing activities efficiently.
# Data Validation:

# Ensure data is valid when adding new books and members, and handle cases where invalid data is entered (e.g., a blank book title or member name).
# Object-Oriented Design:
# Class: Book

# Attributes:
# book_id: Unique identifier for each book.
# title: Title of the book.
# author: Author of the book.
# status: Availability status (available or borrowed).
# Methods:
# __init__(): Initialize the book attributes.
# borrow(): Change the book’s status to borrowed.
# return_book(): Change the book’s status to available.
# Class: Member

# Attributes:
# member_id: Unique identifier for each member.
# name: Name of the member.
# borrowed_books: A list of books currently borrowed by the member.
# max_books: Maximum number of books the member can borrow (3 for Regular, 5 for Premium).
# Methods:
# __init__(): Initialize the member’s attributes.
# borrow_book(): Allow the member to borrow a book, with exception handling for availability and borrowing limit.
# return_book(): Allow the member to return a borrowed book.
# Class: Library

# Attributes:
# book_collection: A collection of all books in the library.
# members: A list of all library members.
# Methods:
# add_book(): Add a new book to the library.
# register_member(): Register a new member.
# lend_book(): Lend a book to a member if it is available.
# receive_return(): Update the status of a returned book.
# Exception Handling:
# Built-In Exceptions:
# Handle common exceptions like:
# ValueError: When invalid input is provided (e.g., trying to borrow a book that doesn’t exist).
# IndexError: When attempting to access non-existent elements in the book or member lists.
# User-Defined Exception:
# Create a custom exception called BorrowLimitExceededException that is raised when a member attempts to borrow more books than their membership type allows.
# Edge Cases:
# Borrowing Unavailable Books:

# What happens if a member tries to borrow a book that is already borrowed by another member?
# Exceeding Borrowing Limit:

# How does the system respond when a regular member attempts to borrow a fourth book or a premium member tries to borrow more than five books?
# Returning Books Not Borrowed:

# What happens if a member tries to return a book they haven’t borrowed?
# Invalid Data Entry:

# What should the system do if the librarian tries to add a book without a title or a member without a name?
class BorrowLimitExceededException(Exception): # Custom Exception for Borrow Limit Exceeded
    def __init__(self, message="Borrow limit exceeded for the member"):
        super().__init__(message)

class Book: # Book Class
    def __init__(self, book_id, title, author, category):
        if not title:
            raise ValueError("The book title should not be empty.")
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.status = 'available'  # 'available' or 'borrowed'

    def borrow(self):
        if self.status == 'available':
            self.status = 'borrowed'
            return f"Book '{self.title}' has been borrowed."
        else:
            raise ValueError(f"Book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            return f"Book '{self.title}' has been returned and is now available."
        else:
            raise ValueError(f"Book '{self.title}' is not currently borrowed.")

    def __str__(self):
        return f"{self.title} by {self.author} ({self.category}) - {self.status}"


class Member:# Member Class
    def __init__(self, member_id, name, max_books):
        if not name:
            raise ValueError("Member name cannot be empty.")
        self.member_id = member_id
        self.name = name
        self.max_books = max_books
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books:
            raise BorrowLimitExceededException(f"{self.name} cannot borrow more than {self.max_books} books.")
        book.borrow()
        self.borrowed_books.append(book)
        return f"{self.name} has borrowed '{book.title}'."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{self.name} has returned '{book.title}'."
        else:
            raise ValueError(f"Book '{book.title}' is not borrowed by {self.name}.")

    def __str__(self):
        borrowed_books_dict = {self.name: [book.title for book in self.borrowed_books]}
        return str(borrowed_books_dict)

# Regular and Premium Member Subclasses
class RegularMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, max_books=3)

class PremiumMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, max_books=5)

# Library Class
class Library:
    def __init__(self):
        self.book_collection = []
        self.members = []

    def add_book(self, book):
        self.book_collection.append(book)
        return f"Book '{book.title}' added to the library."

    def register_member(self, member):
        self.members.append(member)
        return f"Member '{member.name}' has been registered."

    def find_book(self, book_id):
        for book in self.book_collection:
            if book.book_id == book_id:
                return book
        raise ValueError("Book not found in the collection.")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise ValueError("Member not found.")

    def lend_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        return member.borrow_book(book)

    def receive_return(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        return member.return_book(book)

    def __str__(self):
        available_books = [book for book in self.book_collection if book.status == 'available']
        return f"Library has {len(available_books)} available books."

# Testing the system

library = Library()

# Adding Books
print(library.add_book(Book(1, "Mystical Heart", "Balaji", "Fiction")))
print(library.add_book(Book(2, "Hobby", "Harish", "Non-Fiction")))
print(library.add_book(Book(3, "Python Programming", "Sai", "Non-Fiction")))
print(library.add_book(Book(4, "Data Science", "Rahul", "Non-Fiction")))

# Registering Members
regular_member = RegularMember(1, "Kowshik")
premium_member = PremiumMember(2, "Bob")
print(library.register_member(regular_member))
print(library.register_member(premium_member))

# Borrowing Books
try:
    print(library.lend_book(1, 1))  # Kowshik borrows "Mystical Heart"
    print(library.lend_book(2, 2))  # Bob borrows "Hobby"
    print(library.lend_book(2, 3))  # Bob borrows "Python Programming"
except Exception as e:
    print(e)

# Returning Books
try:
    print(library.receive_return(1, 1))  # Kowshik returns "Mystical Heart"
except Exception as e:
    print(e)

# Trying to borrow more than the limit
try:
    print(library.lend_book(1, 1))  # Kowshik borrows "Mystical Heart" again
    print(library.lend_book(1, 2))  # Kowshik borrows "Hobby"
    print(library.lend_book(1, 3))  # Kowshik borrows "Python Programming"
    print(library.lend_book(1, 1))  # Kowshik tries to borrow another book, exceeding limit
except BorrowLimitExceededException as e:
    print(e)
except Exception as e:
    print(e)
# View Library and Member Status
print(library)
print(regular_member)
print(premium_member)
#****************************************************************#
# Output: section

# Book 'Mystical Heart' added to the library.
# Book 'Hobby' added to the library.
# Book 'Python Programming' added to the library.
# Book 'Data Science' added to the library.
# Member 'Kowshik' has been registered.
# Member 'Bob' has been registered.
# Kowshik has borrowed 'Mystical Heart'.
# Bob has borrowed 'Hobby'.
# Bob has borrowed 'Python Programming'.
# Kowshik has returned 'Mystical Heart'.
# Kowshik has borrowed 'Mystical Heart'.
# Book 'Hobby' is already borrowed.
# Library has 1 available books.
# {'Kowshik': ['Mystical Heart']}
# {'Bob': ['Hobby', 'Python Programming']}