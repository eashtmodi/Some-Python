import string

Username=str(input("Username: "))
Password=str(input("Password: "))

letterCondition=string.ascii_letters
symbolCondition=string.punctuation
digitCondition=string.digits



for i in range(len(symbolCondition)):
    if symbolCondition[i] in Username:
        print('invalidUsername')

for i in range(len(letterCondition)):
    if letterCondition[i] in Password:
        break
    else:
        print("InvalidPassword")
        break

for i in range(len(symbolCondition)):
    if symbolCondition[i] in Password:
        break
    else:
        print("InvalidPassword")
        break

for i in range(len(digitCondition)):
    
    if digitCondition[i] in Password:
        break
    else:
        print("InvalidPassword")
        break

        