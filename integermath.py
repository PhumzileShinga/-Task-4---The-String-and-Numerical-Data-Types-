# integermath.py created by Phumzile Shinga

# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate the sum of all the numbers
sum_all = num1 + num2 + num3
print(f"\nThe sum of all the numbers: {sum_all}")

# Calculate the first number minus the second number
difference = num1 - num2
print(f"The first number minus the second number: {difference}")

# Calculate the third number multiplied by the first number
product = num3 * num1
print(f"The third number multiplied by the first number: {product}")

# Calculate the sum divided by the third number
# Avoid division by zero
if num3 != 0:
    division = sum_all / num3
    print(f"The sum of all three numbers divided by the third number: {division}")
else:
    print("Cannot divide by zero. The third number is 0.")
