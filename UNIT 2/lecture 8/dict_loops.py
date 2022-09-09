#30th July 2022

#looping

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}

print("Printing Keys :-")
for x in car:
    print(x)

print("\nPrinting Values :-")
print("Method 1 :-")
for x in car:
    print(car[x])

print("Method 2 :-")
for x in car.values():
    print(x)

#check value presence
print("\nChecking value presence :-")
if "Ford" in car.values():
    print("Ford is present in the dictionary")
else:
    print("Ford is not present in the dictionary")

print("\nCopying the dictionary :-")
car2 = car.copy()
print(car2)

