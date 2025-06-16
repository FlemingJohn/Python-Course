# Dictionary = a collection of {key:value} pairs
# Ordered and changeable. No duplicates

capitals = {

    "usa" : "Dc",
    "india" : "new delhi",
    "china" : "beijing",
    "russia" : "moscow"
}


# print(dir(capitals))
print(help(capitals))

# geting the values of the dict  
print(capitals.get("india"))

if capitals.get("Russia"):
    print("The capital exist")

else:
    print("That capital exist")

# updating the dict 
capitals.update({"Germany": "Berlin"})
capitals.update({"USA":"detroit"})
print(capitals)

# Removing the dict
capitals.pop("china")
capitals.popitem()
print(capitals)

# print keys only
keys =  capitals.keys()
print(keys)

# printing keys using loop
for key in capitals.keys():
    print(key)

# print values 
values = capitals.values()
print(values)

# printing values using loop
for value in capitals.values():
    print(value)

# getting the items both key and value in dict
items = capitals.items()
print(items,"<-ITEMS")

# getting both items in loop 
for key, value in capitals.items():
    print("Key->",key)
    print("Value ->",value)