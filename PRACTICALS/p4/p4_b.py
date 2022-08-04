#wap to print a specified list after removing the 0th, 2nd, 4th and 5th element

print("***********************************************************")
print("Program to remove 0th, 2nd, 4th and 5th element from a list")
print("***********************************************************")

emplist = []     #empty list
print("Enter 10 elements in a list :-")

for i in range(10):
    print("Enter element",i+1,":-",end=" ")
    element = input()
    emplist.append(element)

print("List before removing elements :-",emplist)

emplist.pop(5)
emplist.pop(4)
emplist.pop(2)
emplist.pop(0)

print("List after removing elements :-",emplist)