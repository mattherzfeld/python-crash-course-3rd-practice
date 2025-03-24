#use of f-strings and methods

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

message = (f"Hello, {full_name.title()}!")
print(message)

# using escape sequences

print("\nPython") #newline
print("\tPython\n") #tab
print("Languages:\n\tPython, \n\tC, \n\tJavaScript\n")

# more examples
print("This is a string with a newline character: \nNext line")
print("This is a string with a tab character: \tTabbed text")
print("This string contains a backslash: \\")
print("This string contains a double quote: \"")

# quotes inside of a string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)