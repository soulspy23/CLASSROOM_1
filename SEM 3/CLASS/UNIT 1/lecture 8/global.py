#2nd July 2022

#global keyword

x = "awesome" #global
def myfunc():
    x = "fantastic" #local
    print("Python is " + x)

myfunc() #depends on call
print("Python is " + x)