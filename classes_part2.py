from classes import Car
#The import statement tells Python to open the classes module and import the class Car

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Another example
from classes import Car, ElectricCar

my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

