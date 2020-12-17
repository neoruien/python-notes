## Write a program to print out all the numbers from 0 to 20
## That aren't divisble by 3 or 5
## Note that 0 is considered divisible by everything

# Using continue
for x in range(0, 21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

print("*" * 15)

# Without using continue
for x in range(0, 21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
