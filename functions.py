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

# Positional Arguments

"""The simplest way to  
    do this is based on the order of the arguments provided. Values matched 
    up this way are called positional arguments."""

def describe_pet(animal_type, pet_name): 
    """ Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")

# Keyword Arguments
  # This is a name-value pair that you pass to a function.
def describe_pet(animal_type, pet_name): 
    """ Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster", pet_name="harry") #keyword arguments demonstrate that order does not matter
describe_pet(pet_name="harry", animal_type="hamster")

# Default Values

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie') #animal_type is already defaulted to "dog"

# Equivalent Function Calls

describe_pet("willie")
describe_pet(pet_name="willie")

print("-------- BUFFER --------")

describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")

