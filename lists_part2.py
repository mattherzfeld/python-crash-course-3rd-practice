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

#even_numbers
even_numbers = list(range(2,11,2)) #we can pass a third argument which is a "step" indicator
print(even_numbers)

#square_numbers
squares = []
for value in range(1,11):   #list loops from ints 1 to 10
    square = value ** 2     #set square variable to listed number times itself
    squares.append(square)  #add to end of squares list 

print(squares)

#more conscise square_numbers
squares1 = []
for value in range(1,11):
    squares1.append(value ** 2)

print(squares1)

#simple statistics with a list of ints
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions (allows you generate code in ONE line)
squares = [value ** 2 for value in range(1, 11)]
print(squares)

#4-3 Counting to Twenty
one_to_twenty = [value + 1 for value in range(0, 20) ]
print(one_to_twenty)

#4-4 One Million
#one_to_million = [value + 1 for value in range(0, 999_999)]
#print(one_to_million)

#4-5 Summing a Million
one_to_million = [value + 1 for value in range(0, 999_999)]
print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))

#4-6 Odd Numbers
odd_numbers = list(range(1, 20, 2))
for value in odd_numbers:
    print(value)

#4-7 Threes
multiples_of_three = list(range(3, 31, 3))
for value in multiples_of_three:
    print(value)

#4-8 Cubes
cubes = []
for value in range(1, 11):
    cubed = value ** 3
    cubes.append(cubed)

print(cubes)

#4-9 Cube Comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

#Slicing a List
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) #starts at index zero and stops at index 3(omits 3, does not include)
print(players[1:4])
print(players[:4])  #starts at index zero by default
print(players[2:])  #ends at final index (includes all)
print(players[-3:]) #prints the last three items in the list

#Looping thru a List
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#proof that the two lists are indeed separate -
my_foods.append("cannoli")
print(my_foods)
print(friend_foods)