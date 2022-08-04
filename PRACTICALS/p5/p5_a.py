#write a python script to sort (asc/des) a dictionary by value
#4th Aug 2022

print("*********************************")
print("Program to sort dictionary values")
print("*********************************\n")


d1 = dict() #empty list
num = int(input("How many key-value pairs do you wish to enter for season-1: "))

#loop
for i in range(num):
    data = input("Enter player name and goals seperated by ':' - ")
    tempInput = data.split(':')
    d1[tempInput[0]] = int(tempInput[1])

#printing dictionary
print("Original Dictionary :", d1)
print("Ascending Order : ", sorted(d1.values()))
print("Descending Order : ", sorted(d1.values() , reverse=True))