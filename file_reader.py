from pathlib import Path

#The below would work if the text file was directly in the workspace
#path = Path('pi_digits.txt')

#However, it is located in text_files folder, so we need the below:

#Needed to use 'r' to make it a raw string, which tells Python to interpret backslashes as literal characters.
path = Path(r"C:\Users\Matt\Documents\GitHub\text_files\pi_digits.txt")
#This is the absolute path
#YOU should really use forward slashes instead of backslashes for file paths to avoid this problem.

contents = path.read_text()
contents = contents.rstrip() #read_txt returns an empty string at the end when it reaches end of file
#print(contents)

#Alternatively for the above, we could have simply applied the method immediately.
#This is called, method chaining:
#contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ""
for line in lines:  
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))


#An example of an input program - IF we had downloaded the actual million digits of Pi program -
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# 10-1

path_1 = Path(r"C:\Users\Matt\Documents\GitHub\text_files\learning_python.txt")
contents_1 = path_1.read_text()
print(contents_1)

# 10-2

contents_1 = path_1.read_text().replace("Python", "C") #replacing Python with C by using method chaining
print(contents_1)


# 10-3

#path = Path('pi_digits.txt')
#contents = path.read_text()

#for line in contents.splitlines(): #this is more concise that what we originally used
#  print(line)

# Writing to a File
from pathlib import Path

path = Path("programming.txt") #this writes/creates a new text file
path.write_text("I love programming.") 

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path("programming.txt")
path.write_text(contents)

