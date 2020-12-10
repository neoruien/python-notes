age = 24

print("My age is " + str(age) + " years") # tedious to coerce every int into str

print("My age is {0} years".format(age)) # replacement field {0} is replaced by the first value in the format list

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec")) # multiple replacement fields

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31)) # rearranging (its String.format() but better!)