class school():
    Name=None
    Age=None
    def __init__(self):
        pass
    def name(self,Name):
        self.Name=Name
        print(self.Name)
    def age(self,Age):
        self.Age=Age
        print(self.Age)

class teacher(school):
    Salary=None
    def __init__(self):
        pass
    def salary(self,Salary):
        self.Salary=Salary
        print(Salary)

class student(school):
    Fee=None
    def __init__(self):
        pass
    def fee(self,Fee):
        self.Fee=Fee
        print(Fee)





aman=teacher()
aman.name("AmanDeep")
aman.age("28")
aman.salary("3000")

Easht=student()
Easht.name("Easht Modi")
Easht.age("15")
Easht.fee("1000")
