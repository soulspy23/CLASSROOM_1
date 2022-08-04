#in operator
print("In/not in Operator:-")
v = ("a","b","c","d","e","f","g","h","i","j")
if "a" in v:
    print("'a' is in tuple")

if "k" not in v:
    print("'k' is not in tuple")

#change tuple values
print("\nChanging tuple values:-")
y=list(v)
y[0]="x"
v=tuple(y)  
print("Tuple after changing value:-",v)

#adding, removing tuple values will involve the same process as list

#deleting tuple
print("\nDeleting tuple:-")
y=(12,23,34,45)
del y

#unpacking tuple
#print("\nUnpacking tuple:-")
#g =("a","b","c")
#g = (p,q,r)
#print(p)
#print(q)
#print(r)

#join tuple
print("\nJoin tuple:-")
t = ("a","b","c")
p = (1,2,3)
o = t + p
print("Tuple after joining:-",o)

#multiply tuple
print("\nMultiply tuple:-")
z = t*2
print("Tuple after multiplying:-",z)

