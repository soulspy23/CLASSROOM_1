#accept a string from user. Display its length and display even position alphabets.

str = input("Enter a string :")
x = len(str)
print("Length of string is :",x)
print("Even position alphabets are :")
for i in range(1,x,2):
    print(str[i])