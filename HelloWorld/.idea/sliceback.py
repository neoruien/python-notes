letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # this slice starts at index 25, ends at index 0+1, has a step of -1
print(backwards) # up to and not including index 0

backwards = letters[0:25:-1] # negative step --> start val should be less than stop val
print(backwards) # nothing gets printed

backwards = letters[25:-1:-1] # letters[25] == letters[-1]
print(backwards) # nothing gets printed

backwards = letters[25::-1] # negative step --> start val defaults to end, stop val default to start
print(backwards)

backwards = letters[::-1] # python idiom
print(backwards)

print("\nChallenge: Creating slices")
backwards = letters[16:13:-1]
print(backwards)
backwards = letters[4::-1]
print(backwards)
backwards = letters[:26-8:-1]
print(backwards)

print("\nRevisting slicing without steps")
print(letters[-4:]) # prints the last 4 characters
print(letters[-1:]) # prints the last character
print(letters[:1]) # prints the first character
print(letters[0]) # prints the first character

print("\nQuiz")
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5]) # slice starts at the 1st character and includes every 5th character