# Use a for loop, and augmented assignment,
# to give `answer` the result of multiplying `number` by `multiplier`
# Make sure it works with different values for `number` and `multiplier`

number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
  answer += number

print(answer)