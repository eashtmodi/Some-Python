import csv


with open("data.csv", newline='') as file:

    reader=csv.reader(file)

    file_data=list(reader)

file_data.pop(0)

new=[]

for i in range(len(file_data)):
    num=file_data[i][1]

    new.append(float(num))

# calculating mean
n=len(new)
total=0
for x in new:
    total+=x

mean=total/n

print(mean)


