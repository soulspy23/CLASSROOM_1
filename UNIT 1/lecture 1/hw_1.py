#q1 - write few lines about advantages of python using print statement
print("Question 1:")
print("Advantages of python :")
print("1. It is a high level language")
print("2. It is a object oriented language")
print("3. It have short hand operators")
print("4. It have many built in functions")
print("5. It is an open source language")
print("6. It has wide application architecture")
print("7. It auto-detects datatype")
print("8. It have libraries")

#q2 - WAP to determine whether a number is divisible by number specified by user
print("\nQuestion 2:")

x = int(input("Enter a number :"))
y = int(input("Enter denominator :"))

if (x%y == 0):
    print(x,"is divisible by",y)
else:
    print(x,"is not divisible by",y)