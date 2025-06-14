# Caluculator 

operator = input("Enter an operator: ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print("Addition: ",result)

elif operator == "+":
    result = num1 + num2
    print("Addition: ",result)

elif operator == "-":
    result = num1 - num2
    print("Subtraction: ",result)

elif operator == "*":
    result = num1 * num2
    print("Multiplication: ",result)

elif operator == "/":
    result = num1 + num2
    print("Division: ",result)

else:
    print("Not a valid operator")