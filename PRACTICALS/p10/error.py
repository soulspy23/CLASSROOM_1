#17th Aug 2022

print("**********")
print("Name Error")
print("**********")

def error1():
    try:
        print(x)
    except:
        print("Variable Not Found\n")
error1()

print("***********")
print("Index error")
print("***********")

def error2():
    try:
        l1-[1,2,3]
        print(l1[3])
    except:
        print("Element Not Found\n")
error2()

print("*******************")
print("Zero Division Error")
print("*******************")

def error3():
    try:
        a=12
        b=12/0
        print(y)
    except:
        print("Wrong Calculation\n")
error3()

print("***********")
print("Value error")
print("***********")

def error4():
    try:
        x=int(input("enter a number:"))
        print(x)
    except:
        print("The input should be an int value\n")
error4()

print("*********")
print("Key Error")
print("*********")

def error5():
    try:
        dict={"a":"A",
              "b":"B"}
        print(dict[3])
    except:
        print("Key Not Found\n")
error5()

print("*********************")
print("Module not find error")
print("*********************")

def error6():
    try:
        import asd
    except:
        print("Check the module name again\n")
error6()


#print("*****************")
#print("Indentation Error")
#print("*****************")

# def error7():
#     try:
#         print("hello")
#         except:
#         print("indentation error")
#error7()