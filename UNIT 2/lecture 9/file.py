#file handling

print("File 1 :")
f = open("f.txt", "w") #write in file
f.write("Hello World !")
f=open("f.txt", "r") #read from file

print("Reading 7 characters from file :", f.read(7)) #read 7 characters
print("Reading whole line :",f.readline()) #read whole line

f.close() #close file

#looping through file
print("\nFile 2 :")
f = open("f1.txt", "w")
f.write("I am Shravani Patil.")
f.write("I am in SYBCA.")
f.close()

print("File 2 looping :")
for x in open("f1.txt"):
    print((x))