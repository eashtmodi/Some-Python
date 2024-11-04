print("WELCOME TO SBI BANK")
cardNumber=input("PLEASE ENTER CARD NUMBER: ")
cardPass=input("PLEASE ENTER PASSWORD: ")
balance=int(input("PLEASE TELL YOUR BALANCE: "))

class atm():
    def __init__(self,balace):
        self.balance=balance
    
    def withdrawl(self,withDrawAmount):
        self.balance=self.balance-withDrawAmount
        print(self.balance)

    def increase(self,increase):
        self.balance=self.balance+increase
        print(self.balance)

    def showBalance(self):
        print(self.balance)

atm1=atm(balance)
while(1):
    print("TRY:",("balance","withdraw","increase"))
    task=input("What to do?: ")
    if(task=="balance"):
        atm1.showBalance()
    elif(task=="withdraw"):
        x=int(input("ENTER WITHDRAWL AMOUNT: "))
        atm1.withdrawl(x)
    elif(task=="increase"):
        y=int(input("ENTER INCREASE AMOUNT: ")) 
        atm1.increase(y)  
    else:
        print("TRY THE FOLLOWING KEYWORDS ONLY") 
    