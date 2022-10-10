#13th July 2022

#accept an email id from user and identify whether it belongs to educational domain.
str  = input("Enter e-mail:- ")
if(str.strip().endswith(".edu")):
    print(str,"belongs to educational domain !")
else:
    print(str,"does not belongs to educational domain !")