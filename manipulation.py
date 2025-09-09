# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Calculate and display the length of the sentence
length = len(str_manip)
print(f"\nLength of the sentence: {length}")

# Find the last letter and replace all occurrences with '@'
last_letter = str_manip[-1]
replaced_str = str_manip.replace(last_letter, '@')
print(f"\nString after replacing '{last_letter}' with '@':\n{replaced_str}")

# Print the last 3 characters in reverse
last_three_reversed = str_manip[-3:][::-1]
print(f"\nLast 3 characters reversed: {last_three_reversed}")

# Create a five-letter word from the first 3 and last 2 characters
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"\nNew 5-letter word: {five_letter_word}")
