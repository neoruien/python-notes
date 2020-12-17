import random as rand

highest = 10
answer = rand.randint(1, highest)
print(answer)

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
  if guess == 0:
    print("Thank you for playing the game!")
    break;
  elif guess < answer:
    print("Please guess higher")
  else: # guess must be greater than answer
    print("Please guess lower")
  guess = int(input())

if guess != 0:
  print("Well done, you got it. The answer is {}.".format(answer))