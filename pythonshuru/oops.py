class school():
    name=None
    age=None
    grade=None
    def __init__(self):
        print("object made")
    def info(self,name,age,grade):
        self.name=name
        print(self.name)
        self.age=age
        print(self.age)
        self.grade=grade
        print(self.grade)
    
student1= school()
student1.info("Easht Modi",15,10)

student2= school()
student2.info("Rajeev",28,12)

student3= school()
student3.info("Lalu Yadav",50,1)

student4= school()
print(student4.info("Arvind Kejriwal",35,12))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

