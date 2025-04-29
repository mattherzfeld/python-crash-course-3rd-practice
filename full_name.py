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

#Whitespace
favorite_language = "Python "
print(favorite_language)
print(len(favorite_language))

#removes whitespace - the "r" stands for whitespace to the RIGHT
favorite_language = favorite_language.rstrip()
print(len(favorite_language))

#for the left
x = " Python"
print(len(x))
x = x.lstrip()
print(len(x))

#removeprefix method
nostarch_url = "http://nostarch.com"
nostarch_url = nostarch_url.removeprefix("http://")
print(nostarch_url)

