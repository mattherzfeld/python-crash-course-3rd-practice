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

"""

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

# 7-7
"""
x = 1
while x <= 5:
    print(x)

"""

