#parameter -> for customization

#no return type with parameter 
print("Example 1 :")
def my_funct(x):
    print(5*x)

my_funct(3)
my_funct(5)
my_funct(9)

print("\nExample 2 :")
def func(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
func(fruits)