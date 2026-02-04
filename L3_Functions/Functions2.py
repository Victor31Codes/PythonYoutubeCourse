def main():
    name = input("Hello, What's ur name? ").strip().title()
    hello(name)


def hello(name): #Def is used to define a function
    print("Hello", name + "!")

main()