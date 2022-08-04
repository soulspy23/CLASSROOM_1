#dictionary functions

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}

#get values
print("Values in dictionary :-")
x = car.values()
print(x)

#get items
print("\nItems in dictionary :-")
y = car.items()
print(y)

#check key exist or not
print("\nChecking key exist or not :-")
if "color" in car:
    print("Color is present in the dictionary")
else:
    print("Color is not present in the dictionary")

#change values
print("\nChanging values in dictionary :-")
car["color"] = "brown"
print(car)

#update values
print("\nUpdating values in dictionary :-")
car.update({"color": "black"})
print(car)

#removing items
print("\nRemoving items from dictionary :-")
car.pop("brand")
print(car)

#delete item
print("\nDeleting item from dictionary :-")
del car["color"] #deletes key-value pair
print(car)

#clear dictionary
print("\nClearing dictionary :-")
car.clear()
print(car)
