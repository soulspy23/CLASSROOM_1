#number of arguments are uncertain, add * before argument name

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Mithil","Srihari","Rishabh")