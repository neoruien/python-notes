low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
  print("\tGuessing in the range of {} to {}".format(low, high))
  guess = low + (high - low) // 2
  high_low = input("My guess is {}. Should I guess higher or lower? "
                   "Enter h or l, or c if my guess was correct: "
                   .format(guess)).casefold()

  if high_low == "h":
    # Guess higher. The low end of the range becomes 1 greater than the guess.
    low = guess + 1
  elif high_low == "l":
    # Guess lower. The high end of the range becomes one less than the guess.
    high = guess - 1
  elif high_low == "c":
    print("I got it in {} guesses!".format(guesses))
    break
  else:
    print("Please enter h, l or c")

  # guesses = guesses + 1
  # Python creates a new variable and binds it to the calculation result,
  # then destroys the original variable

  guesses += 1
  # augmented assignment (more efficient)
  # performs the operation in-place where possible,
  # modifying the original variable

pass # placeholder for real code