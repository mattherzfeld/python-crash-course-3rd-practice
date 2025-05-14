# Classes

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


#Making an Instance from a Class
my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Accessing Attributes
my_dog.name

#Calling Methods
my_dog.sit()
my_dog.roll_over()

#Creating Multiple Instances
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()

# 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the two attribute information"""
        print(f"The restaurant's name is {self.restaurant_name} and serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """indicate that the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is open.")
    
my_restaurant = Restaurant("Chick Fil-A", "southern chicken")
print(f"\nThe restaurant's name is {my_restaurant.restaurant_name}.")
print(f"\nThe restaurant's type of food is {my_restaurant.cuisine_type}.")
my_restaurant.describe_restaurant()
print(f"\nIs {my_restaurant.restaurant_name} open or closed?")
my_restaurant.open_restaurant()

# 9-2

restaurant_one = Restaurant("Taco Bell", "Mexican")
restaurant_two = Restaurant("McDonald's", "American/Burger")
restaurant_three = Restaurant("Hattie B's", "Southern Chicken")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()

# 9-3
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUser Information:")
        print(f"\tFirst Name: {self.first_name}")
        print(f"\tLast Name: {self.last_name}")
        print(f"\tAge: {self.age}")
        print(f"\tLocation: {self.location}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"\nHello, {self.first_name} {self.last_name}!")

#Instances
person_one = User("David", "Lynch", 41, "Chicago, IL, USA")
person_two = User("Jane", "Bobowski", 47, "Seattle, WA, USA")
person_three = User("Maria", "Gonzales", 33, "Mexico City, Mexico")
person_four = User("Javier", "Rodriguez", 22, "Madrid, Spain")

#Method Calls
person_one.greet_user()
person_one.describe_user()
person_two.greet_user()
person_two.describe_user()
person_three.greet_user()
person_three.describe_user()
person_four.greet_user()
person_four.describe_user()


#Working with Classes and Instances

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Prints  statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 9-4
    # Starting with program from exercise # 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """prints the two attribute information"""
        print(f"The restaurant's name is {self.restaurant_name} and serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """indicate that the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is open.")
    
    def set_number_served(self, customers):
        """Sets the number of customers that have been served"""
        self.number_served = customers
    
    def increment_number_served(self, customers_served):
        """Increments the number of customers who have been served"""
        self.number_served += customers_served

restaurant = Restaurant("In-N-Out", "Burgers")
print(f"\nThe {restaurant.restaurant_name} serves {restaurant.cuisine_type}.")
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.set_number_served(5)
print(f"The restaurant has now served {restaurant.number_served} customers.")
restaurant.increment_number_served(12)
print(f"The restaurant has now served {restaurant.number_served} customers.")