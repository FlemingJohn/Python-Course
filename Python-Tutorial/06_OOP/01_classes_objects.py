# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex: phone, cup, book
# You need a "class" to create many objects

# class  = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model 
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car")
        print(f"You drive the {self.model}")
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print("You stop the car")
        print(f"You stop the {self.model}")
        print({f"You stop the {self.color} {self.model}"})

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mustan",2024,"red",False)
car2 = Car("ford",2025,"red",True)
car3 = Car("Benz",2026,"red",False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car2.for_sale)