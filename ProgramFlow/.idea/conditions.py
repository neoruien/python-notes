age = int(input("How old are you? "))

# if age >= 16 and age <= 65: # this chained comparison can be simplified
if 16 <= age <= 65:
  print("Have a good day at work")
else:
  print("Enjoy your free time")
# and: Python stops checking as soon as it finds a False condition

print("-" * 20)

if age < 16 or age > 65:
  print("Enjoy your free time")
else:
  print("Have a good day at work")
# or: Python stops checking as soon as it finds a True condition