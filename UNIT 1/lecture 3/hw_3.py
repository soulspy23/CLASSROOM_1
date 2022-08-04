#nested loop for multiplication table
# 11 12 13           
# 22 24 26
# 33 36 39

for x in range(1,11):
    for y in range(11,14):
        print(x*y,end=" ")
    print()

print()

for i in range(1,11):
    for j in range(12,31,2):
        print(i*j,end=" ")
    print()