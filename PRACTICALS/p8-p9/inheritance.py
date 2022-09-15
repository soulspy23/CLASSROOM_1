#Inheritance in Python
print("***************************")
print("Using Inheritance in python")
print("***************************")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printDetails(self):
        print("Hello! I am a Person")
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, Class, rollNo):
        Person.__init__(self, name, age)
        self.Class = Class
        self.rollNo = rollNo
    def printDetails(self):
        print("----------------------")
        print("Hello! I am a Student")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Class:", self.Class)
        print("RollNo:", self.rollNo)

class businessMan(Person):
    def __init__(self, name, age, companyName, Income):
        Person.__init__(self, name, age)
        self.companyName = companyName
        self.Income = Income
    def printDetails(self):
        print("--------------------------")
        print("Hello! I am a Business Man")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company Name:",self.companyName)
        print("Income:",self.Income,"Rupees")

class MBAStudent(Student):
    def __init__(self, name, age, Class, rollNo, collegeName):
        Student.__init__(self, name, age, Class, rollNo)
        self.collegeName = collegeName
    def printDetails(self):
        print("------------------------")
        print("Hello! I am a MBA Student")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Class:",self.Class)
        print("RollNo:",self.rollNo)
        print("College Name:",self.collegeName)

p1=Person("Uday",19)
p1.printDetails()

s1=Student("Ronit",12,"10th",69)
s1.printDetails()

b1=businessMan("Raj",27,"Wipro",88000.00)
b1.printDetails()

m1 =MBAStudent("Shravani", 19, "MBA", 47 ,"SKSC")
m1.printDetails()