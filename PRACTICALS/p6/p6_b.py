#Write a Python program to read last n lines of a file.

print("*********************************************\n")
print("Python program to read last n lines of a file")
print("*********************************************\n")

f = open("test.txt","w")
f.write("Names of fruits: \n1)Apple \n2)Banana \n3)Cherry \n4)Pineapple \n5)Papaya \n6)Blueberry")
f.close()

f = open("test.txt","r")
content = f.readlines()
n = int(input("Enter the number of lines you want to read:"))

print("Content :")
for x in content[-n:]:
    print(x,end="")

f.close()