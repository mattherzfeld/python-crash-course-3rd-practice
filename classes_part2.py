from classes import Car
#The import statement tells Python to open the classes module and import the class Car

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Another example
from classes import ElectricCar as EC #importing under an alias

my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = EC("nissan", "leaf", 2024) #used the alias
print(my_leaf.get_descriptive_name())

# 9-10
    #Skipped as it is just importing module practice

# 9-11

from classes import Privileges as Priv
from classes import Admin as Ad

admin_example = Ad("Bobby", "Boucher", 29, "Florida")

admin_example.privileges.show_privileges()

# 9-12

from classes import User as US

The_guy = US("Robert", "Diamond", 25, "New Orleans, LA")

The_guy.greet_user()
The_guy.describe_user()

# Python Standard Library

from random import randint
print(randint(1, 6))

from random import choice
players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(first_up)

# 9-13

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(f"Rolling the die...\nResult: {number}.")

#Create a 6-sided die
six_sided_die = Die()

#Roll the die 10 times
print("\n\nRolling the die: \n")

for number in range(10):
    six_sided_die.roll_die()

# 9-14

from random import choice

# Possible lottery selections
lottery_characters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

# List that will have the 4 winning elements
winning_characters = []

while len(winning_characters) < 4:
    character = choice(lottery_characters)

    # Prevent any duplication of winning_characters
    if character not in winning_characters:
        winning_characters.append(character)

# Display and selection winning characters:
print("Here are today's winning lottery numbers:")

for character in winning_characters:
    print(character)

# 9-15

my_ticket = ["C"]

#initialize the number of times the following for loop runs:
count = 0

for ticket in winning_characters:

    count += 1

# 9-16
    # This exercise centers around exploring the Python Standard Library
    # https://pymotw.com

import time #time is a fun/important module to import

print("Python is thinking...")
time.sleep(5) #This will then wait 5 seconds
print("Aha! After further consideration, Python is still the best language!")

