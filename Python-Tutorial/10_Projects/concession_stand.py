# Concesion is nothing but menu items 

# menu -> collection of food items
menu = {
    "dosa": 30,
    "idly":40,
    "poori":60,
    "rosemilk":89,
    "badammilk":90
}

# cart to store the buyed foods
cart = []

# total represents the no of food
total = 0

print("---MENU---")
for key, value in menu.items():
    print(f"{key:10}:{value} ")

# Decorator
print("----------")

while True:
    food =  input("Select an item(q to quit):").lower()
    if food == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)
    
    else:
        print("Items not available")

# print your orders after adding to the cart 
print("---Your Order ---")


for food in cart:
    total += menu.get(food)
    print(f"Food: {food}")

print() #adding space to the output
print("Total of your food is: ",total)