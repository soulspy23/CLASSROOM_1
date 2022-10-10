#30th June 2022
#accept a string from user and check if it is a palindrome
num = int(input("Enter a number: "))

temp = num
sum = 0
while num > 0:
    rem = num % 10
    sum = sum*10 + rem
    num = int(num/10)

if(sum==temp):
    print("Palindrome")
else:
    print("Not a palindrome")