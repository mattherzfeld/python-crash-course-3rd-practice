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
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

del(motorcycles[0])
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#3-4 Guest List
guestList = ["Tiger Woods", "Vladimir Lenin", "Otto von Bismarck"]
print(f"Dear {guestList[0].title()}, please come to my dinner party.")
print(f"Dear Comrade {guestList[1].title()}, you are cordially invited to my dinner party.")
print(f"Dear Mr. {guestList[2].title()}, you are invited to my dinner party. Please come.")

#3-5 Changing Guest List
cannot_make_it = "Otto von Bismarck"
guestList.remove(cannot_make_it)
print(f"\nUnfortunately, {cannot_make_it.title()} can no longer attend the dinner party.")
guestList.append("Theodore Roosevelt")
print(f"Dear {guestList[2].title()}, please consider attending my dinner party. Thank you!")
print(guestList)

#3-6 More Guests
guestList.append("Bill Walton")
guestList.insert(0, "Steven Spielberg")
guestList.insert(2, "Vincent Price")
print(guestList)
print(f"Dear Guests, a new table has become available and now we will be a party of 7")

#3-7 Shrinking Guest List
    #I'm going to cheat and use a while loop to shorten my codebase:
while len(guestList) > 2:
    poppedGuest = guestList.pop()
    print(f"I'm sorry, {poppedGuest.title()}. I can no longer extend an invite to the dinner party. My apologies.")

print(guestList)
print(f"Hi {guestList[0].title()}, I am pleased to inform you are still invited to the dinner party.")
print(f"Hi {guestList[1].title()}, I am pleased to inform you are still invited to the dinner party.")

#Clear out the list and print to double check
del(guestList[:])
print(guestList)

#Sorting lists (permanently)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #alphabetical order
print(cars)
cars.sort(reverse=True) #reverse alphabetical order
print(cars)

#Sorting lists (temporarily)
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print(len(cars))

#3-8 Seeing the World
locations = ["Bali", "Mexico City", "Ho Chi Minh City", "Kuala Lumpur", "Auckland"]
print(locations)
print(sorted(locations))
print(locations) #to prove sorted function was temporary
print(sorted(locations, reverse=True))
print(locations) #to prove sorted function was temporary
locations.reverse()
print(locations)
locations.reverse()
print(locations) #back to original order
locations.sort()
print(locations) #should be alphabetical
locations.sort(reverse=True)
print(locations) #should be reverse alphabetical

#3-9 Dinner Guests
print(len(guestList)) #because we cleared out that list
print(len(locations)) #audibled and showed number of locations

#3-10 Every Function
unvisitedStates = ["Alaska", "Montana", "Idaho", "North Dakota", "Wyoming", "New Mexico", "Oklahoma", "Kansas", "Delaware", 
                   "West Virginia", "Maine", "New Hampshire", "Vermont"]
print(unvisitedStates)
print(len(unvisitedStates))

#Indexing
new_motorcycles = ["honda", "yamaha", "suzuki"]
print(new_motorcycles[-1]) #returns last item of list

#list1 = []
#print(list1[-1]) - this will error out