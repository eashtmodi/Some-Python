try:
    age=int(input("Tell your age"))
except:
    print("Please only numbers")
else:
    print("Your age is {}".format(age))
finally:
    print("executed")