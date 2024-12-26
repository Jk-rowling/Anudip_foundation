#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

# Taking input from the user
number = int(input("Enter a number: "))

# Using ternary operator to check if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

# Printing the result
print(f"The number {number} is {result}.")

-----------------------------------------------------------------------------

#2.2. Using input function take two number and then swap the number

# Taking input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Displaying the numbers before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping the numbers
num1, num2 = num2, num1

# Displaying the numbers after swapping
print(f"After swapping: num1 = {num1}, num2 = {num2}")

