print('Python is interesting')
print('Printing "quotes" in strings')
print("Printing another type of 'quotes' in strings")

greeting = "Hello"
name = input("Please enter your name ")
print(greeting + ' ' + name)

# Dynamic typing
age = 24
print(type(age)) # int --> bind the name/label/variable age to the int value
age = "2 years"
print(type(age)) # string --> rebind the label age to the string value

# Strong typing
name = "Sarah Tan"
age = 20
print(name + " is " + age + "years old") # error