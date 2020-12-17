number = input("Please enter a series of numbers, using any separators you like: ") # "9,223;372:036 854,775;807"
separators = ""

for char in number:
  if not char.isnumeric():
    separators += char

values = "".join(char if char not in separators else " " for char in number).split()

print(separators)
print([int(val) for val in values])
print(sum([int(val) for val in values]))

## Extracting capitals
quote = """"
  Alright, but apart from the Sanitation, the Medicine, Education, Wine,
  Public Order, Irrigation, Roads, the Fresh-Water System,
  and Public Health, what have the Romans ever done for us?
"""
capitals = ""

for char in quote:
  if char.isupper():
    capitals += char

print(capitals)