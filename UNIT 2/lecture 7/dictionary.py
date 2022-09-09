#27th July 2022

#dictionaries

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Dictionary:-",thisdict)

print("\nLength of dictionary:-",len(thisdict))

print("\nType:-",type(thisdict))

print("\nPrinting dictionary keys:-")
x = thisdict.keys()
print(x)

print("\nAdding new key and value:-")
thisdict["color"] = "red"
print("After adding :-",thisdict)

#if key exist it will update the value
#if key doesn't exist it will add the key and value

