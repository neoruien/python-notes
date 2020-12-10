for i in range(1, 13):
  print("{0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# can provide any expression inside the format parantheses
# exponent operator: i ** 2 == i to the power of 2

print()

for i in range(1, 13):
  print("{0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# better formatting of field width - right alignment

print()

for i in range(1, 13):
  print("{0:2} squared is {1:<3} and cubed is {2: <4}".format(i, i ** 2, i ** 3))

# better formatting of field width - left alignment

print()

for i in range(1, 13):
  print("{0:2} squared is {1:^3} and cubed is {2: ^4}".format(i, i ** 2, i ** 3))

# better formatting of field width - center alignment

print()

for i in range(1, 13):
  print("{} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

# 3rd field still uses the colon to control the layout, even if you haven't specified a field number
# if field numbers are not provided, a value cannot be used more than once
# The order in which values are used cannot be changed too

print()

print("Field width of 12: {0:12}".format(22 / 7))
print("Precision of 12 decimals: {0:12f}".format(22 / 7))
print("Field width of 12, precision of 50 decimals: {0:12.50f}".format(22 / 7)) # precision is prioritized over field width
print("Field width of 52, precision of 50 decimals: {0:52.50f}".format(22 / 7))
print("Field width of 62, precision of 50 decimals: {0:62.50f}".format(22 / 7))
print("Field width of 72, precision of 50 decimals: {0:72.50f}".format(22 / 7))
print("Field width of 72, precision of 50 decimals: {0:<72.54f}".format(22 / 7)) # max float precision is 52 digits, remaining digits are padded with zeros