from re import X


def my_function():
    global x
    x = "fantastic"

my_function()
print("Python is " + x)