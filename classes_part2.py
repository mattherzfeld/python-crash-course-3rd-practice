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


