#10th Aug 2022

#examples
print("Exception Handling :")
print("Example 1 :")
try:
    print(x)
except:
    print("X is not defined")

print("\nExample 2 :")
try:
    print(x)
except NameError:
    print("Variable X is not defined !")
except:
    print("Something else went wrong !")

#else keyword
print("\nUse of else keyword :")
try:
    print("Hello !")
except:
    print("Something Went Wrong !")
else:
    print("Nothing went wrong !")

#finally keyword
print("\nUse of finally keyword :")
try:
    print('x')
except:
    print("Something Went Wrong !")
else:
    print("Else block !")
finally:
    print("Finisheddd !!!")