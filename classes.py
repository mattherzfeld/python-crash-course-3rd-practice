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
        pass

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        pass
