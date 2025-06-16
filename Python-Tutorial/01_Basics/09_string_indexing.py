# Indexing = accessing elements of a sequence using [] (indexing operator)
# Syntax: [start : end : step]

name = input("Enter the some string char: ")

# print the first value only
print(name[0]) 

# print form 0 to before the index of 4
print(name[0:4])
print(name[:4])

# from start to end index
print(name[4:8])

# only from start index
print(name[4:])

# getting the last value
print(name[-1])

# getting the last four characteres
print(name[-4:])

# stepping every 2 element
print(name[::2])

# stepping every 3 element 
print(name[::3])

# Excersise 1 Return the last 4  digits of your Credit card
credit_card = input("Enter the credit card number: ")
print("Last 4 digits of the credit number: ",credit_card[-4:])

# Excersise 2 Reverse your phone number
phone_number = input("Enter the phone Number: ")
print("Reversed phone no: ",phone_number[::-1])