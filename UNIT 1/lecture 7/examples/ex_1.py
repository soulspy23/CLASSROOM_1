#accept a number from user and display its divisor from 1 to 10.

num = int(input("Enter a number: "))
for i in range(1,11):
    if num%i == 0:
        print(i)