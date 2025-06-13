# Type casting = The process of converting a value of one data type to another
# (string, integer, float, boolean)
# Explicit vs Implicit

# Explicit - direct data type decalaration
name = "Fleming"
age = 21
gpa = 1.9
student = True

# type - define what type of data
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# Implicit - Conver from one data type to another data type
age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

name = bool(name)
print(name)