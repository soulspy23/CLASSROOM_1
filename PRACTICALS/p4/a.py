#wap that takes 2 lists and returns True if they have atleast one common member
#28th July

l1= [] #empty list
no =int(input("How many elements you wish to enter for list-1 :-"))
print("\nEnter",no,"elements for list-1 :-")

for i in range(no):
    print("Enter element",i+1,"for list-1 :-",end=" ")
    element=input()
    l1.append(element)

l2= [] #empty list
no1 =int(input("\nHow many elements you wish to enter for list-2 :-"))
print("\nEnter",no1,"elements for list-2 :-")

for i in range(no1):
    print("Enter element",i+1,"for list-2 :-",end=" ")
    element=input()
    l2.append(element)

def ChkCommon(l1,l2):
    if(len(l1)<len(l2)):
        arg1 = l1
        arg2 = l2
    else:
        arg1 = l2
        arg2 = l1
        
    for x in arg1:
        if x in arg2:
            return True
    return False

if(ChkCommon(l1,l2)):
    print("\nYes, there are elements in common.")
else:
    print("\nNo, there aren't elements in common.")