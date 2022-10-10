#19th July 2022

#insert
list = ["apple","banana","cherry"]
list.insert(2,"watermelon")
print("\nInserting 1 item at 2nd index:- ",list)

#list within list
print("\nList within list:-")
list.insert(2,["mango","grapes"])

#extend list
print("\nExtending list:-")
l1=[12,23,34]
l2=["a","b","c"]
l1.extend(l2)
print("extended list:-",l1)

#remove element
print("\nRemoving element:-")
list.remove("apple")
print("Removed element:-",list)

#remove element by index
print("\nRemoving element by index:-")
l1.pop(1) #with index
l1.pop() #without index
print("Removed element:-",l1)

#clear list
print("\nClearing list:-")
list.clear()
print(list)

#delete list
print("\nDeleting list:-")
del list

#sorting
print("\nSorting list:-")
l=[12,23,34,45,56,67,78]
l.sort()
print("Sorted list:-",l)
l.sort(reverse=True)
print("Sorted reversed list:-",l)

x=["a","X","B","g"]
print(x)
x.sort()
x.sort(key=str.lower)

#copy
print("\nCopy list:-")
l5 = l.copy()
print(l5)

#list function
list = list(l5)

#join list
print("\nJoin list:-")
v =  x + l5

