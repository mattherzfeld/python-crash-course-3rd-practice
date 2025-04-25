# While Loops
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)


# Using a Flag
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)


# Using a Break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == "quit":
        break #exits the loops without any additional code being called
    else:
        print(f"I'd love to go to {city.title()}!")

# Using 'Continue' in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #returns to the beginning of the loop

    print(current_number)

# 7-4
prompt = "\nPlease enter the toppings that you wish to be on your pizz:"
prompt += "\nWhen finished, please enter 'quit' to exit. "

while True:
    toppings = input(prompt)

    if toppings == "quit":
        break
    else:
        print("\nI'll be sure to add that topping to your pizza. Anything else?")

# 7-5
prompt = "\nWelcome to Cheap-o Cinemas! We need your age in order to calculate the price of your ticket."
prompt += "\nHow are old are you? "

while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("Your ticket if FREE.")

    elif age < 12:
        print("That will be $10 please.")

    else:
        print("That will be $15 please.")

    break



# 7-6

prompt = "\nWelcome to Cheap-o Cinemas! We need your age in order to calculate the price of your ticket."
prompt += "\nHow are old are you? "


# 1st Exit -
while True:
    age = input(prompt)
    age = int(age)

    if age == 0:
        print("Are you sure if you are actually alive?!?!")
        break
    if age < 3:
        print("Your ticket if FREE.")

    elif age < 12:
        print("That will be $10 please.")

    else:
        print("That will be $15 please.")

    break

# 2nd Exit -
active = True

while active:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("Your ticket if FREE.")
        active = False
    elif age < 12:
        print("That will be $10 please.")
        active = False
    else:
        print("That will be $15 please.")

    break

# 3rd Exit -
while True:
    age = input(prompt)

    if age == "quit":
        break

    else:
        age = int(age)

    if age < 3:
        print("Your ticket if FREE.")

    elif age < 12:
        print("That will be $10 please.")

    else:
        print("That will be $15 please.")

    break
"""
# 7-7
"""
x = 1
while x <= 5:
    print(x)

"""

# Using a while loop with lists/dictionaries

# users that need to be confirmed
unconfirmed_users = ["alice", "brian", "candace"]
# initial empty list for confirmed users
confirmed_users = []

# use pop method to take last unconfirmed user and assign to current_user variable
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    # print statement saying verifying that popped user and append it to the confiremed_user list
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of specific values from a list

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# Loops thru removing each instance of "cat" until none are left and exits loop
while "cat" in pets:
    pets.remove("cat")

print(pets)

# Filling a dictionary with user input

# Start with an empty dictionary where we will end up storing participant's name and response
responses = {}

polling_active = True # Set Flag

while polling_active:
    # Prompt for the person's name/response
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb someday? ")

    # Store the response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to be taking the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# Polling is complete / show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# 7-8

"""

sandwich_orders = ["club", "italian", "meatball", "blt", "vegetarian"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich == "blt":
        print(f"I have finished making your {current_sandwich.upper()} sandwich.")
    else:
        print(f"I have finished making your {current_sandwich.title()} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandiwches have been prepared:")
for current_sandwich in finished_sandwiches:
    if current_sandwich == "blt":
        print(current_sandwich.upper())
    else:
        print(current_sandwich.title())

"""

# 7-9

sandwich_orders = ["club", "pastrami", "italian", "pastrami", "meatball", "blt", "pastrami", "vegetarian"]

finished_sandwiches = []

print("Sorry, we actually ran out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("I removed pastrami from your sandwich list.")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich == "blt":
        print(f"I have finished making your {current_sandwich.upper()} sandwich.")
    else:
        print(f"I have finished making your {current_sandwich.title()} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandiwches have been prepared:")
for current_sandwich in finished_sandwiches:
    if current_sandwich == "blt":
        print(current_sandwich.upper())
    else:
        print(current_sandwich.title())

# 7-10

responses = {}

polling_active = True # Set Flag

while polling_active:
    # Prompt for the person's name/response
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, where would you go? ")

    # Store the response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to be taking the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# Polling is complete / show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")