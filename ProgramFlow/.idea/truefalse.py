day = "Friday"
temperature = 30
raining = False

# `and` has a higher precedence than `or`
# add parentheses to make the code clearer
if (day == "Saturday" and temperature > 27) or not raining:
  print("Go swimming")
else:
  print("Learn Python")

## Built-in objects that are considered as False

if 0: # 0 is evaluated to False in a boolean expression
  print("True")
else:
  print("False")

name = ""
if name: # Empty string is evaluated to False in a boolean expression
  print("Hello, {}".format(name))
else:
  print("Are you the man with no name?")