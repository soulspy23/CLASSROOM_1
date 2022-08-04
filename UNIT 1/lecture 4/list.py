#for loop for list

fruits = ["apple", "banana", "cherry"]
print("Example 1 :")
for x in fruits:
    print(x)

print("\nExample 2 :")
for x in "banana":
    print(x)

#exit
print("\nExample 3 :")
for x in fruits:
    print(x)
    if x == "banana":
        break

#skip the list
print("\nExample 4 :")
for x in fruits:
    if x == "banana":
        continue
    print(x)
     