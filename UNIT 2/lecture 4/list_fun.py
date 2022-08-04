#lists

list1=["stats","DBMS","OS","python","VR"]
print("OG List:- ",list1)

print("\nFirst indexed item:- ",list1[1])

print("\nLength of list:- ",len(list1))

print("\nLast indexed item:- ",list1[-1])

print("\nPrint 1st and 2nd item:- ",(list1[1:3])) #exclude last item mentioned

print("\nPrint until 2nd item:- ",(list1[:3])) #exclude last item mentioned

print("\nPrint from item 1:- ",(list1[1:])) #includes first item

print("\nPrint from last index to 4th last index:- ",(list1[-4:-1])) #negative indexing

print("\nin operator:-")
if "os".upper() in list1:
    print("OS is present in list")
else:
    print("OS is not present in list")

print("\nReplace items:-")
print("Before replacing:-",list1)
list1[1]="SPM"
print("After replacing 1st item:- ",list1)

