#while loop

print("Example 1 :")
i = 1
while i <6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#exit loop when i is 3
print("\nExample 2 :")
x = 1
while x<6:
    print(x)
    if x == 3:
        break
    x+=1

#continue loop when x is 3
print("\nExample 3 :")
y = 0
while y<6:
    y+=1
    if y == 3:
        continue
    print(y)
    