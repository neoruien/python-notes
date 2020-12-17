## Initializing

print("Please choose your option from the list below:")

options = ['Learn Python', 'Learn Java', 'Go swimming', 'Have dinner',
           'Go to bed', 'Exit', 'Learn machine learning', 'Listen to music',
           'Reply to messages']

options_string = ""

for index in range(len(options)):
    options_string += '{}. {}'.format(index + 1, options[index]) + '\n'

print(options_string)

## My method

choice = int(input("Choose an option: "))

while True:
    if choice > len(options):
        choice = int(input("This option is invalid. Please choose again from the list below:\n" + options_string))
        continue
    else:
        if choice == 0:
            print("Goodbye")
            break
        else:
            print("You chose to: {}".format(options[choice - 1]))
    choice = int(input("Choose an option: "))

## Alternative
choice = "-"
while choice != "0":
    if choice in "123456789":
        print("You chose {}".format(choice))
    else:
        print(options_string)
    choice = input()