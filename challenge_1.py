# challenge_1.py created by Phumzile Shinga

import math

# Ask the user to enter the lengths of all three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Calculate the semi-perimeter
s = (side1 + side2 + side3) / 2

# Use Heron's formula to calculate the area
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Print the area
print(f"\nThe area of the triangle is: {area:.2f}")