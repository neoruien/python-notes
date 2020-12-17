answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

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

tree1 = input("Please provide the name of your first tree: ")
tree2 = input("Please provide the name of your second tree: ")
if tree1 == tree2:
  print("The trees are the same")
else:
  print("The trees are different")

x = 5
y = 7
if x > y:
  print("x is greater than y")
elif x < y:
  print("x is smaller than y")
else:
  print("x equals y")