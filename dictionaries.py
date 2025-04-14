# Dictionaries
# Key-Value pairs
import os, time

alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary

alien_1 = {}

alien_1["color"] = "red"
alien_1["points"] = 10

print(alien_1)

# We can simply modify dictionary values

alien_1["color"] = "yellow"

print(f"The alien's color is now {alien_1["color"]}.")

alien_2 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_2["x_position"]}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_2["speed"] == "slow":
    x_increment = 1
elif alien_2["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_2["x_position"] = alien_2["x_position"] + x_increment

print(f"New position: {alien_2["x_position"]}")

# Removing a key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")


alien_0 = {"color": "green", "speed": "slow"}
#print(alien_0["points"])

# ^ we get a syntax error because the key we asked for does not exist.
# if there's a chance of the above occurring, try using the get() method

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# 6-1
person1 = {
    "first_name": "Denise",
    "last_name": "Smith",
    "age": 43,
    "city": "Las Cruces",
}

print(person1)

# 6-2
favorite_numbers = {
    "Paul": 77,
    "Jerome": 63,
    "Dennis": 91,
    "Michael": 23,
    "Scottie": 33,
}

print(f"Michael's favorite number is {favorite_numbers['Michael']}.")

# 6-3



# Looping thru a dictionary

# Cleans up your terminal after viewing output
#time.sleep(10) #10 second delay before clearing
#os.system('cls')