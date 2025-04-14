cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "bmw"
# conditional test, checks for equality (if true, prints true (boolean))
print(car == "bmw")
car = "audi"
print(car == "bmw")

#prints false as Python is case sensitive
car = "audi"
print(car == "Audi")

#prints true
car = "Audi"
print(car.lower() == "audi")

request_topping = "mushroom"

# inequality operator
if request_topping != "anchovies":
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again")

# Using and to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# Using or to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) #prints true due to age_0 being greater than or equal to 21

# using the keyword "in"
request_toppings = ["mushroom", "onions", "pineapple"]

print("mushroom" in request_toppings) #prints True due to the the inquired topping being in the list
print("pepperoni" in request_toppings) #prints False ""

# checking whether something is NOT in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.") # not in keyword

# Boolean expressions
game_active = True
can_edit = False

# if statements
age = 18
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18.")

# if-elif-else chain

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost if $40.")

# more efficient version:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"You admission cost is ${price}.")

# multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20 #effectively a senior discount

print(f"Your admission cost is ${price}.")

# Testing multiple conditions

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print ("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# only use the if-elif-else chain if you only want one block of code to run**

# 5-3
alien_color = "red"

if alien_color == "green":
    print("Player has just earned 5 points!")

alien_color = "green"

if alien_color == "green":
    print("Play has just earned 5 points!")

# 5-4
alien_color = "red"
if alien_color == "green":
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")

# 5-5
alien_color = "red"
if alien_color == "green":
    print("Player just earned 5 points.")
elif alien_color == "yellow":
    print("Player just earned 10 points.")
else:
    print("Player just earned 15 points.")

# 5-6
age = 35
if age < 2:
    print("You are a baby!")
elif age >= 2 and age < 4:
    print("You are a toddler!")
elif age >= 4 and age < 13:
    print("You are a kid!")
elif age >= 13 and age < 20:
    print("You are a teenager!")
elif age >= 20 and age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")

# 5-7
favorite_fruits = ["blueberries", "mango", "raspberries", "grapes", "bananas"]

if "blueberries" in favorite_fruits:
    print("You really like blueberries!")
if "pears" in favorite_fruits:
    print("You really like pears!")
if "mango" in favorite_fruits:
    print("You really like mango!")
if "grapes" in favorite_fruits:
    print("You really like grapes!")
if "bananas" in favorite_fruits:
    print("You really like bananas!")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

#Checking for special items
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#empty list check
requested_toppings = []

if requested_toppings: #this checks whether the list is actually populated
    for requested_topping in requested_toppings:
        print(f"Adding {request_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#using multiple lists

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni",
                      "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# 5-8
user_names = ["admin", "Matt", "Jordan", "Rory", "Justin", "Bryson"]

for user_name in user_names:
    if user_name == "admin":
        print(f"Hello {user_name}, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")

# 5-9
#defining new list to show how empty list check works
user_names1 = []
if user_names1:
    for user_name1 in user_names1:
        if user_name1 == "admin":
            print(f"Hello {user_name1}, would you like to see a status report?")
        else: 
            print(f"Hello {user_name1}, thank you for logging in again.")
else:
    print("We need to find some users ASAP!")

# 5-10
current_users = ["Matthew", "Mark", "Luke", "John", "Peter", "Paul"]
new_users = ["Matthew", "Simon", "Judas", "Noah", "Isaac", "Luke"]

for new_user in new_users:
    if new_user in current_users:
        print(f"The username ({new_user}) is already taken, you will need to enter a new username.")
    else:
        print(f"That username ({new_user}) is available.")

# 5-11
numbers = list(range(1,11))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    else:
        print(str(number) + "th")

