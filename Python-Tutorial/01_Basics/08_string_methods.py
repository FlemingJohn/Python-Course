# String is a sequence of characters which is used to rperesent the text

name = input("Enter your name: ")

# len() is used to get the length of the string
length = len(name)

# find() is used to get the index first repeating position of the string
index = name.find("f")
print("Positon: ",index)

# rfind is used to get the last repeating position of the string 
last_index = name.rfind("e")
print("Last Index: ",last_index)

# convert a string to captial letter only first letter
captial = name.capitalize()
print("Captial: ",captial)

# convert an entire string to lower
lower = name.lower()
print("Lower :",lower)

# convert an entire string to upper
upper = name.upper() 
print("Upper: ",upper)

# isdigit() this function returns the true if it is digit
digit_or_not = name.isdigit()
print("Is it digit: ",digit_or_not)

# isalpha() this function return false if it is alphalbetic
alpha_or_not = name.isalpha()
print("Is it alpha: ",alpha_or_not)

#count() in string return the totat no of string space in betwee 
space_count = name.count(" ")
print("Total no of spaces: ",space_count)

# replace() this function replace exsiting values with new values
replace_value = name.replace("f"," ")
print("Replace value: ",replace_value)
