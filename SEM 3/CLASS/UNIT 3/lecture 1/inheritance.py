#29th Aug 2022
print("Inheritance :")

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,year,roll_no):
        Person.__init__(self,name,age)
        #self.name = name
        #self.age = age
        self.year = year
        self.roll_no = roll_no

s1 = Student("Shravani", 19, "2nd", 47)
print("\nInformation of Student :")
print("Name of the student :",s1.name)
print("Age of the student :",s1.age)
print("Currently Studying Year :",s1.year)
print("Roll no of student :",s1.roll_no)