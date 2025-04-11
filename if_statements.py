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



