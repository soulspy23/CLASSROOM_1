#initializing tuple
thistuple = ("apple", "banana", "cherry")
print("Tuple :-",thistuple)

print("\nTuple length:-",len(thistuple))

#create tuple with single value
t = ("x",)
print("\nTuple with single value:-",t)

#with multiple data types
t = ("x",1,2.098,True)
print("\nTuple with multiple data types:-",t)

#type
print("\nType of tuple:-",type(t))

#accessing tuple items is done by index
print("\nTuple item at index 0:-",t[0])

#range of indexing
v = ("a","b","c","d","e","f","g","h","i","j")
print("\nTuple:-",v)
print("Tuple item at index 1 to 3:-",v[1:3])
print("Tuple item at index 3 to end:-",v[3:])
print("Tuple item at index 6 from start:-",v[:6])
print("Tuple items from 2nd last indes to 4th last:-",v[-4:-2])
print("\nEmpty Tuple:-",v[-2:-4])

