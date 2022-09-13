#29th August 2022

#Always assign default values to variables which are actually requiring such assignment
#eg.size,dimension

print("Assigning default values in class :")
class Person:
    name = "XYZ"
    age = 14
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,year,roll_no):
        self.year = year
        self.roll_no = roll_no

s1 = Student("3rd",23)
print("Name of the student :",s1.name)
print("Age of the student :",s1.age)
print("Currently studying year :",s1.year)
print("Roll Number :",s1.roll_no)