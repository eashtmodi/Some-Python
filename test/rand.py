import random
print("Guess Karna Game")
chances=5
number=random.randint(0,9)
while(chances>0):
    guess=int(input("Guess Kar Na"))
    if(guess<number):
        print("Think Bigger")
    elif(guess>number):
        print("Not That Big!")
    elif(guess==number):
        print("Wah Ji Wah!")
    chances=chances-1
    continue
    

if(chances==0):
    print("har gaya haha")

input("Enter To Exit")