d1 = dict() #empty list
num = int(input("How many key-value pairs do you wish to enter for football season-1: "))

#loop
for i in range(num):
    data = input("Enter player name and goals seperated by ':' - ")
    tempInput = data.split(':')
    d1[tempInput[0]] = int(tempInput[1])

print("\nSeason-1 Scores :", d1)

d = input("Name the key you wish to delete :")
d1.pop(d)

print("\nSeason-1 Scores after deleting:", d1)