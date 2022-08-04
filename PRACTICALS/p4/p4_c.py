#wap to clone or copy a list

l1= [] #empty list
no =int(input("How many elements you wish to enter for list-1 :-"))
print("\nEnter",no,"elements for list-1 :-")

for i in range(no):
    print("Enter element",i+1,"for list-1 :-",end=" ")
    element=input()
    l1.append(element)

print("\nList-1:-",l1)

l2 = l1.copy()
l2.append("copy")

print("\nThe copied list:- ",l2)