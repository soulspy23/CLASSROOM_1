#write a python script to concatenate following dictionaries to create a new one

print("****************************************************")
print("Program to concatenate given dictionaries in new one")
print("****************************************************\n")

d1 = dict() #empty list
num = int(input("How many key-value pairs do you wish to enter for season-1: "))

#loop
for i in range(num):
    data = input("Enter player name and goals seperated by ':' - ")
    tempInput = data.split(':')
    d1[tempInput[0]] = int(tempInput[1])

d2 = dict() #empty list
num2 = int(input("\nHow many key-value pairs do you wish to enter for season-2: "))

#loop
for j in range(num2):
    data2 = input("Enter player name and goals seperated by ':' - ")
    tempInput2 = data2.split(':')
    d2[tempInput2[0]] = int(tempInput2[1])

#concatenation
print("\nSeason-1 Scores :", d1)
print("\nSeason-2 Scores :", d2)

tempDict = d1.copy()
tempDict.update(d2)

print("\nAll scores :", tempDict)