answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
  if guess < answer:
    print("Please guess higher")
  else: # guess must be greater than answer
    print("Please guess lower")
  guess = int(input())
  if guess == answer:
    print("Well done, you guessed it")
  else:
    print("Sorry, you have not guessed correctly")
else:
  print("You got it first time")

# Reordered
if guess == answer:
  print("You got it first time")
else:
  if guess < answer:
    print("Please guess higher")
  else: # guess must be greater than answer
    print("Please guess lower")
  guess = int(input())
  if guess == answer:
    print("Well done, you guessed it")
  else:
    print("Sorry, you have not guessed correctly")

# Code with duplication
if guess < answer:
  print("Please guess higher")
  guess = int(input())
  if guess == answer:
    print("well done, you guessed it")
  else:
    print("Sorry, you have not guessed correctly")
elif guess > answer:
  print("Please guess lower")
  guess = int(input())
  if guess == answer:
    print("Well done, you guessed it")
  else:
    print("Sorry, you have not guessed correctly")
else:
  print("You got it first time")

# Comparing strings with ==
tree1 = input("Please provide the name of your first tree: ")
tree2 = input("Please provide the name of your second tree: ")
if tree1 == tree2:
  print("The trees are the same")
else:
  print("The trees are different")