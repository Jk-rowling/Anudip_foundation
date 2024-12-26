#1. Python Program to Find the Largest Among Three Numbers (Using nested if)


#input three number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

---------------------------------------------------------------------------------


#A transport company charges the fare according to following table:
#Distance Charges
#1-50 	8 Rs./Km
#51-100 	10 Rs./Km
#> 100 	12 Rs/Km

#Write a program to input distance travelled as input and calculate and print the total charge.
#Use comments where necessary and follow python naming conventions.


# Function to calculate the total fare based on the distance traveled
def calculate_fare(distance):
    if distance <= 50:
        fare = distance * 8  # 8 Rs./Km for distance 1-50 Km
    elif distance <= 100:
        fare = (50 * 8) + (distance - 50) * 10  # 10 Rs./Km for distance 51-100 Km
    else:
        fare = (50 * 8) + (50 * 10) + (distance - 100) * 12  # 12 Rs./Km for distance > 100 Km
    return fare

# Input the distance traveled from the user
distance_traveled = float(input("Enter the distance traveled (in Km): "))

# Calculate the total fare
total_fare = calculate_fare(distance_traveled)

# Print the total fare
print(f"The total fare for {distance_traveled} Km is: {total_fare:.2f} Rs.")

