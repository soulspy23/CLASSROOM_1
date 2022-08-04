#for loop
print("For Loop :-")

l3=[23,34,45,56,67,78]
for i in l3:
    print(i)

#while loop
print("\nWhile Loop :-")
i=0
while i<len(l3):
    print(l3[i])
    i+=1

#looping through comprehension
print("\nLooping through comprehension :-")
[print (x) for x in l3]

