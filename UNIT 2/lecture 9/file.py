#file handling

f = open("f.txt", "w") #write in file
f.write("Hello World !")
f=open("f.txt", "r") #read from file

print("Reading 7 characters from file :", f.read(7)) #read 7 characters
print("Reading whole line :",f.readline()) #read whole line
