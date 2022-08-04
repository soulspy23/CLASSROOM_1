#uppercase
print("Example 1:- ")
x = "Shravani"
print(x.upper())

#lowecase
print("\nExample 2:- ")
print(x.lower())

#strip function -> delete spaces
print("\nExample 3:- ")
str = "     Hello World !    "
print(str.strip())

#replace function
print("\nExample 4:- ")
print(x.replace("i","e"))

#string concatenation
print("\nExample 5:- ")
a ="Uday"
b= "Rane"
c = a+b
print(c)

#split function
#print("\nExample 6:- ")
#print(a.split("",""))

#string format
print("\nExample 7:- ")
age = 36
txt = "My name is Shravani, I am " + age
print(txt)

print("/nExample 7'a':- ")
txt1= "My name is Shravani, I am {}"
print(txt1.format(age))

print("/nExample 7'b':- ")
q = 3
n = 567
p = 46.95

t = "I want to pay {2} dollars for {0} pieces of item {1}."
print(t.format(q,n,p))