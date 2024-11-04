class calculator():
    x=None
    y=None
    def __init__(self):
        print(" ")
    def add(self,x,y):
        print(x+y)
    def minus(self,x,y):
        print(x-y)
    def mul(self,x,y):
        print(x*y)
    def div(self,x,y):
        print(x/y)

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print("press 1 to add  2 to sub  3 to mul  4 to div ")

function=input(str())

calc=calculator()
if function=="1":
    calc.add(num1,num2)
if function=="2":
    calc.minus(num1,num2)
if function=="3":
    calc.mul(num1,num2)
if function=="4":
    calc.div(num1,num2)

    
