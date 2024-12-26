# Write a program to take the diamater of a circle as user input and calculate and print its area & circumference.
import math

# Take the diameter of the circle as user input
diameter = float(input("Enter the diameter of the circle: "))

# Calculate the radius
radius = diameter / 2

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Calculate the circumference of the circle
circumference = 2 * math.pi * radius

# Print the area and circumference
print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")

