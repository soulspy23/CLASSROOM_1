#29th Aug 2022

#create Class
class MyClass:
    x=5

#create objects
print("\nCreate Objects :")
p1 = MyClass()
print(p1.x)

#__init__ function gets invoked while creating objects, with parameters(constructor)
print("\nInvoking init function :")
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def myfunc(self):
        print("Hello ! My name is",self.name)
        print("I am",self.age,"years old !")
        print("My gender is", self.gender)
    def delete(self):
        print("Hello ! My name is",self.name)
        print("I am",self.age,"years old !")

p1 = Person("Shravani", 19, "Female")
p1.myfunc()

#modify obj prop
print("\nModifying object properties :")
p1.age = 40
print("Modified age :",p1.age)

#delete obj prop
print("\nDeleting object property:")
del p1.gender
p2 = ("Uday", 10)
p1.delete()