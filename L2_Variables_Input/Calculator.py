x = input("What's your x?")
y = input("What's your y?")

z = int(x) + int(y)
print("The result is: " + str(z))
print(z)

"""Another example with another way to do it, or putting functions into functions"""
x = int(input("What's your x?"))
y = int(input("What's your y?"))

z = x + y
print("The result is: " + str(z))
print(z)


x = float(input("What's your x?"))
y = float(input("What's your y?"))

z = round(x + y)
print("The result is: " + str(z))
print(f"{z:,}") #|Using f-strings to format numbers with commas as thousands separators

z = round(x / y, 2) #Rounding to 2 decimal places
print(f"{z:,.2f}") #Using f-strings to format numbers with commas and 2 decimal places

