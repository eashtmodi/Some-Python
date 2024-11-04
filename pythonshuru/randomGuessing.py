import random
x=random.randint(0,100)

while 1:
    num=int(input("Guess from 0 to 100: "))
    if num<x:
        print("Entered number is small")
    if num>x:
        print("Entered number is big")
    if num==x:
        print("You won!")
        break