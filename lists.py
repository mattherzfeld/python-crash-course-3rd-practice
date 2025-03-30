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