# Weight converter

weight = float(input("Enter the wight:"))
unit = input("Kilograms or Pounds? (k or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight,1)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weigth is :{round(weight,1)} {unit}")

else:
    print(f"{unit} was not valid")
