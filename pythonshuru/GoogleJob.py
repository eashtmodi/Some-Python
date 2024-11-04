li=["Apple","Berry","Banana","Grapes","Apple","Berry"]
li.sort()
x=1
print(li)
for i in li:
    if x<=(len(li)-1)           :
        if i==li[x]:
            print(str(i))
        else:
            pass
        x=x+1