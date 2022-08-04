# write a python program to sum of all the items in the dictionary

print("***********************************")
print("Program to sum values of dictionary")
print("***********************************\n")

d1 = dict() #empty list
num = int(input("How many key-value pairs do you wish to enter for season-1: "))

#loop
for i in range(num):
    data = input("Enter player name and goals seperated by ':' - ")
    tempInput = data.split(':')
    d1[tempInput[0]] = int(tempInput[1])

#adding values
sum=0
for x in d1.values():
    sum=sum+x

#printing values
print("\nThe list of scores in season-1 :", d1)
print("\nSum of all scores in season-1 is :", sum)