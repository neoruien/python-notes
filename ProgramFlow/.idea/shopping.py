shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

for item in shopping_list:
    if item != "spam":  # we don't like spam so we skip it
        print("Buy " + item)

print("*" * 15)

for item in shopping_list:
    if item == "spam":  # we don't like spam so we skip it
        continue

    print("Buy " + item)

print("*" * 15)

for item in shopping_list:
    if item == "spam":  # we stop shopping
        break

    print("Buy " + item)
