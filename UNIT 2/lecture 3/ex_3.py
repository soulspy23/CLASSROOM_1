#finding whether the string is a palindome

str = input("Enter a string for palindrome :- ")
newstr = ""
len = len(str)
while(len>0):
    newstr = newstr+str[len-1]
    len = len-1

if(str==newstr):
    print("The string is a palindrome !")
else:
    print("The string is not a palindrome !")