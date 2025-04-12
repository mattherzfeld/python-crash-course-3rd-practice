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




