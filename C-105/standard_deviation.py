import math
import csv 

with open("data.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data.pop(0)

def mean(data):
    frequency=len(data)
    total=0
    for x in data:
        total=total+int(x)
    mean=total/frequency
    return mean

squaredList=[]
for n in data:
    a=int(n)-mean(data)
    a=a**2
    squaredList.append(a)