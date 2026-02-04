def hello(to="world"): #Def is used to define a function
    print("Hello", to + "!")

hello() #Calling the function without arguments

name = input("Hello, What's ur name? ").strip().title()
hello(name)
