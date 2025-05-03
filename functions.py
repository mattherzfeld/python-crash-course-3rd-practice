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

#A dog named Willie
describe_pet("willie")
describe_pet(pet_name="willie")

print("-------- BUFFER --------")

#A hamster named Harry
describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")

# 8-3

def make_shirt(size, text):
    print(f"\nThe shirt you selected is size {size} and says, \"{text}\".")

make_shirt(size="Large", text="Cheers fellas!")
make_shirt("Medium", "Hookin' Horns!")

# 8-4

def make_shirt(size="Large", text="I love Python."):
    print(f"\nThe shirt you selected is size {size} and says, \"{text}\".")

make_shirt() #default
make_shirt(size="Medium") #new size with default message
make_shirt(size="Small", text="I love Java.") #new size with new message

# 8-5

def describe_city(city, country="Germany"):
    print(f"\n{city} is in {country}.")

describe_city("Berlin")
describe_city(city="Munich", country="Germany")
describe_city(city="Chicago", country="the United States")

# Return Values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# Making an Argument Optional

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("john", "lee", "hooker")
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("john", "booty", "david")
print(musician)

# Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person("jimi", "hendrix")
print(musician)

def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "hendrix", age = 27)
another_musician = build_person("paul", "mccartney") #age remains default
print(musician)
print(another_musician)

# Using a function with a while loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

"""THIS IS AN INFINITE LOOP
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
"""
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q'  at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 8-6

def get_city_country(city, country):
    """Returns city/country pairs as a String"""
    cc_pair = f"{city}, {country}"
    return cc_pair.title()

visit1 = get_city_country("Santiago", "Chile")
visit2 = get_city_country("Chicago", "USA")
visit3 = get_city_country("Mexico City", "Mexico")
print(visit1)
print(visit2)
print(visit3)

# 8-7

def make_album(artist, album, track=None):
    """Returns a dictionary containing artist name / album title"""
    music = {"Artist Name": artist, "Album Title": album}
    if track:
        music["track"] = f"Number of Tracks: {track}"
    return music

album1 = make_album("Kanye West", "Graduation")
album2 = make_album("The Beatles", "Magical Mystery Tour")
album3 = make_album("Thirty Seconds to Mars", "A Beautiful Lie", 12)

print(album1)
print(album2)
print(album3)

# 8-8

def make_album(artist, album, track=None):
    """Returns a dictionary containing artist name / album title"""
    music = {"Artist Name": artist, "Album Title": album}
    if track:
        music["track"] = f"Number of Tracks: {track}"
    return music

while True:
    print("\nTell me an artist/album:")
    print("(enter 'q'  at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    formatted_artist_album = make_album(artist, album)
    print(f"\nResults:\n\t{formatted_artist_album}!")

# Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

# Modifying a List in a Function

#Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodechedron"]
completed_models = []

#Simulate printing each design until none are left.
#Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#Display all completed models:
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Copying a List
print_models(unprinted_designs[:], completed_models) #the slice notation makes a copy

# 8-9 Messages

def show_messages(messages):
    for message in messages:
        the_message = f"{message}"
        print(the_message)

messages = ["Welcome to Wrexham", "Howdy, folks!", "This is yet another message."]

show_messages(messages)

# 8-10

def show_messages(messages):
    for message in messages:
        the_message = f"{message}"
        print(the_message)

messages = ["Welcome to Wrexham", "Howdy, folks!", "This is yet another message."]
sent_messages = []

while messages:
    current_message = messages.pop()
    print("Sending message...")
    sent_messages.append(current_message)

print("The following messages have now been sent:")
for sent_message in sent_messages:
    print(sent_message)

