for i in range(1, 21):  # 1 (inclusive) to 21 (exclusive)
    print("i is now {}".format(i))

print("*" * 20)

for i in range(10):  # 0 (inclusive) to 10 (exclusive)
    print("i is now {}".format(i))

print("*" * 20)

for i in range(10, 2):  # no values in this range
    print("i is now {}".format(i))

print("*" * 20)

for i in range(0, 10, 2):  # 0 (inclusive) to 10 (exclusive) with a step of 2
    print("i is now {}".format(i))

print("*" * 20)

for i in range(10, 0, -2):  # 10 (inclusive) to 0 (exclusive) with a step of -2
    print("i is now {}".format(i))

print("*" * 20)

for i in range(0, 10, -2):  # no values in this range
    print("i is now {}".format(i))

print("*" * 20)

# Write a program to print out all numbers from 0 to 100 that are divisible by 7
# Note that 0 is considered to be divisible by all other integers

for x in range(0, 101, 7):
    print(x)
