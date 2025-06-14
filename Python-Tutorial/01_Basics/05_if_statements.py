# if statement - Do some code if conditionn is True 
# else statement -  Do something else if above condition are false

# Excersise - 1 
# Question - Find the age 

age = int(input("Enter the age: "))

if age >= 100:
    print("You are too old to sign up")

elif age >= 18:
    print("you are signed up")

elif age < 0:
    print("You are in your moms stomach")
else:
    print("You must be 18+ sign up")

# Excersie - 2 
# Question - do you want food or not 

response = input("Enter the response")

if response == 'Y':
    print("Have some food")

else:
    print("No food for you!")

# Excersie - 3
# Question - name validation

name = input("Enter your name")

if name == "":
    print("You did not enter the name")

else:
    print(f"Hello {name}")

# Excersie - 4
# Question - to chech whether you are in online or not 
online = False

if online:
    print("You are online")

else:
    print("You are offline")

