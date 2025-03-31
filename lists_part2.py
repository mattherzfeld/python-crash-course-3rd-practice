# Lists Part 2 - Working with Lists

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone. That was a great magic show!")

#4-1 Pizzas
pizzas = ["pepperoni", "sausage", "mushroom"]

for pizza in pizzas:
    print(f"We have a {pizza} pizza on the menu.")

print("\nI really love pizza!")

#4-2 Animals
animals = ["dog", "cat", "bird"]
for animal in animals:
    print(f"A {animal} would make a really great pet!")

print("These are all animals that are located at the local pet shop.")

#Using the range() function
for value in range(1, 5): #notice how the second parameter is not included in the actual list
    print(value)

for value in range(6): #if only one parameter used, defaults to starting list at zero
    print(value)

#Using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)