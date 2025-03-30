# Lists - Data Structure examples

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

print(f"My first bicycle was a {bicycles[0].title()}.")

#3-1 Names
names = ["Joel", "Eric", "Alex", "Jake", "Cody", "Caleb", "Spencer"]
print(len(names))

#3-2 Greetings
print(f"{names[3]} is a veteranarian.")
count = len(names)
print(f"The names list has {count} items in it.")

#3-3 Your Own List
cars = ["Honda", "Ford", "Dodge", "Nissan", "Toyota", "Hyundai", "Chevrolet"]
print(f"I'd like to own a {cars[1].upper()}!!")

#Modifying Lists
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles[0] = "Ducati"
print(motorcycles)

motorcycles.append("Honda")
print(motorcycles)

#Two parameters (index, item being added) - does not overwrite "Ducati that was in that index, just moves items back"
motorcycles.insert(0, "Harley-Davidson")
print(motorcycles)

#Deletes indexed item
del(motorcycles[0])
print(motorcycles)

#Removing using pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")