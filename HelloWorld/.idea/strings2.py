parrot = "Norwegian Blue"

print(parrot)

print(parrot[3]) # string is an array

print("\nMini challenge:")
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("\n Positive and negative indexing:")
index = ""
word = ""
for i in range(-14, 14): # 14 is the string length
  index += str(i)
  word += parrot[i]
print(index)
print(word)

print("\nMini challenge (negative indexing):") # negative index = positive index - string length
print(parrot[-11]) # 11 = 3 - 14
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])