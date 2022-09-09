#13th July 2022

#accept a mobile number and test whether it is a valid number in terms of len and char
str = input("Enter contact number :")
if(len(str)==10 and str.isnumeric()):
    print(str,"is a valid contact number !")
else:
    print(str,"is not a valid contact number !")