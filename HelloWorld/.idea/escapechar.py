# =========================================================================
print("PRINTING STRING")

# Printing string with many quotation marks
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# Delimiting strings with \ and newline
unsplitString = """This string has been \
split over \
several \
lines"""
print(unsplitString)
# or
anotherUnsplitString = """The pet shop owner said "No, no, \
'e's uh,...he's resting"."""
print(anotherUnsplitString)

# =========================================================================

print("SPLITTING STRING")

# Splitting string with \n
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# Splitting string with 2 extra quotation marks and newlines
anotherSplitString = """This string has been
split over
several
lines"""
print(anotherSplitString)

# =========================================================================

print("TABBING STRING")

# Adding tabs to string with \t
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# =========================================================================

print("PRINTING SPECIAL CHARACTERS")

# Printing special characters with \
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("C:\\Users\\timbuchalka\\notes.txt")
# or (raw string)
print(r"C:\Users\timbuchalka\notes.txt")