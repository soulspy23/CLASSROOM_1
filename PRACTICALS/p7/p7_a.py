#1st September
#employee

class employee:
    e_total = 0
    #create objects
    def __init__(self,e_id,e_dept,e_desg,e_sal,e_inc):
        self.e_id = e_id
        self.e_dept = e_dept
        self.e_desg = e_desg
        self.e_sal = e_sal
        self.e_inc = e_inc

    #calculate total salary
    def calcSalary(self):
        self.e_total = self.e_sal + self.e_inc

    #display details
    def disp_details(self):
        print("\nDetails Of Employee :-")
        print("Employee Id =", self.e_id)
        print("Employee Department =",self.e_dept)
        print("Employee Designation =",self.e_desg)
        print("Employee Basic Salary =",self.e_sal)
        print("Employee Incentive =",self.e_inc)
        print("Employee Total Salary =",self.e_total)

#take user input
n = int(input("Enter the number of records you wish to add :- "))
counter = 0
emp=[]
for i in range(1,n+1):
    print("Information of Employee",i,":-")
    print("Enter the Id for Employee",i,":-")
    e_id = int(input())
    print("Enter the Department of Employee",i,":-")
    e_dept = input()
    print("Enter the Designation of Employee",i,":-")
    e_desg = input()
    print("Enter the Basic Salary of the Employee",i,":-")
    e_sal = int(input())
    print("Enter the Incentive Amount for Employee",i,":-")
    e_inc = int(input())
    emp.append(employee(e_id, e_dept, e_desg, e_sal, e_inc))

#object listing
for x in range(0,n):
    emp[counter].calcSalary()
    emp[counter].disp_details()
    counter += 1