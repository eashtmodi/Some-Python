class Car(object):
    def __init__(self,model,color,company,speed):
        self.model=model 
        self.company=company
        self.color=color
        self.speed=speed

    def start (self):
        print("Car started!!")
    def stop(self):
        print("Car stoped!!!")
    def accelerating (self):
        print("accelerating")
    def gear_Change(self):
        print("gearChanged")
    def tellCustomization(self):
        print(self.model)
        print(self.company)
        print(self.color)
        print(self.speed)

    

audi= Car("A6","black","audi",50)

print(audi.tellCustomization())
    