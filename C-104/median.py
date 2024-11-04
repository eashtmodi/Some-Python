import csv


with open("data.csv", newline='') as file:

    reader=csv.reader(file)

    file_data=list(reader)

file_data.pop(0)

new=[]

for i in range(len(file_data)):
    num=file_data[i][1]

    new.append(float(num))

# calculating median
n=len(new)

new.sort()

if n%2==0:
    median1=float(new[n//2])
    median2=float(new[n//2 -1])
    median=(median1+median2)/2

else:
    median=new[n//2]

print(median)

