# input() - It is an build-in function used to get the input from the user

name =  input("Enter your name:")
age = float(input("Enter your age:"))

print(f"Hello {name}")
print(f"You are {age} year old")

# Excerise - 1 => Area Calculator

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length*width
print(f"The area is: {area}cm^2")

# Excersis - 2 => Shopping cart 

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price*quantity

print(f"You have bought {quantity} x {item}/s")
print(f"your total is: ${round(total, 2)}")