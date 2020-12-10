string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords") # this works too
print(string1, string2, string3, string4, string5) # adds an additional space in between

print("Hello " * 5) # strings can be multiplied
# print("Hello " * 5 + 4) # strong typing violation --> changing str to int
print("Hello " * (5 + 4)) # string is multiplied 9 times
print("Hello " * 5 + "4") # string is multiplied and then appended to "4"

today = "friday"
print("day" in today) # True, "day" exists in "friday"
print("fri" in today) # True, "fri" exists in "friday"
print("thur" in today) # False
print("parrot" in "fjord") # False

print()