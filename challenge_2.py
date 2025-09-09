# challenge_2.py created by Phumzile Shinga

# Ask the user for the name of their favourite restaurant
string_fav = input("What is your favourite restaurant? ")

# Ask the user for their favourite number and cast it to an integer
int_fav = int(input("What is your favourite number? "))

# Print both values
print("Your favourite restaurant is:", string_fav)
print("Your favourite number is:", int_fav)

# Try to cast the restaurant name to an integer
# This will raise a ValueError because strings that contain letters
# (like a restaurant name) cannot be converted to an integer.

# Uncomment the line below to see the error
# string_to_int = int(string_fav)

# Explanation:
# Trying to cast a non-numeric string (like "Pizza Place") to an integer
# will result in a ValueError because Python cannot convert letters or 
# special characters into a valid number.