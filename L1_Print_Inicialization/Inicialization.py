# Ask for the user's name
name = input ("What's ur name? ") #Creating variables

#Removing leading and trailing whitespace form the str
name = name.strip()

#Capitalizing the first letter of the string
name = name.capitalize()

#Capitalize all the titles
name = name.title()

# Greet the user
print ("Hello, " + name + "!") 

#This is another option only in one line
name = input("Hello, What's ur name? ").strip().title()
"""
Doing comments in python in another way
This is a multi-line comment
docs.python.org/3/tutorial/controlflow.html#documentation-strings

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)"")
This is the structure of the print function that docs python show to us
"""
print("Hello, ", end="") #Using end to avoid the new line
print(name) #The default value of end is \n (new line)

print("Hello 'Friend'") #Using single quotes inside double quotes
print('Hello "Friend"') #Using double quotes inside single quotes
print('Hello \'Friend\'') #Using escape character to use single quotes inside single quotes
print("Hello \"Friend\"") #Using escape character to use double quotes inside double quotes                 

print(f"Hello, {name}!") #Using f-strings to format strings (Python 3.6+)