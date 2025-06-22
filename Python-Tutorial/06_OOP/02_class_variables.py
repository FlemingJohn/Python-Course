# Class variable = shared among all instances of a class defined outside the constructor.
# allow you to share data among all objects created from that class 

class Student:
    class_year = 2025
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age 
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick",35)
student3 = Student("Fleming",21)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
