activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): # casefold() is a better version of lower()
  print("But I want to go to the cinema")