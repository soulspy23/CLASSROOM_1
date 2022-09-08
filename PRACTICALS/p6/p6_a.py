#wap to read an entire text file
#18th aug 2022
try:
    print("*****************************")
    print("Python program to read a file.")
    print("*****************************\n")

    #ask user about file name
    print("Enter file name to be created :")
    fname = input()
    f  = open(fname, "w")

    content = input("Enter text to be written :")
    f.write(content)
    f.close()

    print("Do you wish to append your file (Y/N) :")
    x = input()
    if (x == "Y" or x == "y"):
        f = open(fname,"a")
        content = input("Enter text to be written :")
        f.write(content)
        f.close()
    elif(x == "N" or x == "n"):
        f = open(fname, "r")
        f.close()
    else:
        print("Try again !")

    f = open(fname,"r")
    print("Content :",f.read())
    f.close()

except:
    print("Done with file handling !")