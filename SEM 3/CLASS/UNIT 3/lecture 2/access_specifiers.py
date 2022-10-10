class person:
    def __init__(self, name, age):
        #protected
        self.name = name
        self.age  = age

    def display(self):
        #protected
        print("Name is",self.name,"and age is",str(self.age))

class student(person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show(self):
        self.display()

class MBAstudent(student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def prints(self):
        self.display()

s = MBAstudent("Uday",19)
s.prints()