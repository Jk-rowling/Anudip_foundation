#1.Write a program to input 3 sides of a triangle and calculate and print its area.
a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))

# Calculate the area
area = a*b*c

# Print the area
print(f"The area of the triangle is: {area:.2f}")

------------------------------------------------------------------------------------------

#Write a program to input the temperature in celcius and calculate ans print it in Farhenheit.
celsius = float(input("Enter temperature\
in celsius: "))

fahrenheit = (celsius * 1.8) + 32

print(str(celsius )+ " degree Celsius\
is equal to " + str(fahrenheit )+
	" degree Fahrenheit.")

