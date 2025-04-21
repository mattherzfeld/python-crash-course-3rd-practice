# basic user input setup

message = input("Tell me something and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you are a little older.")

# Modulo Operator
# Divides one number by the other and provides the remainder value
print(4%3) # Answer is 1
print(6%3) # Answer is 0


# Example with if statement
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


