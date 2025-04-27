# Functions

def greet_user():
    """ Display simple greeting"""
    print("Hello!")

greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user("jesse")

# 8-1

def display_message():
    print("I am learning about functions in this chapter.")

display_message()

# 8-2

def favorite_book(book_title): #function name with optional parameter - in this case, "book_title"
    print(f"One of my favorite books is {book_title.title()}.")

favorite_book("Alice in Wonderland")