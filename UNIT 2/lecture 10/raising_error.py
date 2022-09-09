#10th Aug 2022

#in try block keep the argument which gives error
#example 1
x ="Hello"
if not type(x) is int:
    try:
        raise TypeError("Only Integers are allowed !")
    except:
        print("Handles Successfully !")