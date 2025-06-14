# Arithitmetic operators  - It is an basic addition,subtraction,multiplication and divsion methods

friends = 5 

# Addition 
friends = friends+1
friends += 1

# Subtraction
firends = friends-2
firends -= 2

# Multiplication
firends = firends*3
friends *= friends

# Division
friends = friends / 2

print(friends)

# Built in function -> pre written code 

x = 3.14
y = 4 
z = 5 

#Round function 
Round = round(x)
print(Round)

# Absolute function
Absolute = abs(x)
print(Absolute)

# Power function 
Power = pow(4,3)
print(Power)

# Maixmum value
Maximum = max(x,y,z)
print(Maximum)

# Minimum value
Minimum = min(x,y,z)
print(Minimum)

# importing Math module
import math

# pi function 
print(math.pi)

# eulers number 
print(math.e)

# Square root
print(math.sqrt(x))

# ceil function 
print(math.ceil(x))

# Excersise - 1 
# Question - Find the cirumference

radius = float(input("Enter the radius of the circle:"))

cirumference = 2 * math.pi * radius

print(f"The cirucumfernce is: {round(cirumference)}")

# Excersise - 2
# Questions - Find the area of the circle 

Area = math.pi* pow(radius,2)

print(f"Area is {Area}")

# Hypotenus Calculator
# Question find the hypothensus of the triangle 

Side_1 = float(input("Enter the the Side1: "))
Side_2 = float(input("Enter the Side1: "))

Side_3 = math.sqrt(pow(Side_1,2)+pow(Side_2,2))

print(f"Hypothensu of a triangel: {Side_3} cm")