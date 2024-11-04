import csv
from collections import Counter

with open("SOCR-HeightWeight.csv", newline='') as file:
    
    reader=csv.reader(file)

    data=list(reader)

data.pop(0)

new=[]

for i in range(len(file_data)):
    num=file_data[i][1]

    new.append(float(num))

def mean():
    n=len(new)
    total=0
    for x in num:
        total+=x
    Mean=total/n
    print("Mean is "+ Mean)


def median():
    n=len(new)

    new.sort()

    if n%2==0:
        median1=float(new[n//2])
        median2=float(new[n//2 -1])
        Median=(median1+median2)/2

    else:
        Median=new[n//2]

    print(Median)

def mode():
    
    data=Counter(new)

    modeOfDataForRange={
        '50-60':0
        '60-70':0
        '70-80':0
    
    }

    for height, occurence in data.items():
        if 50 < float(height) < 60:
            mode_data_for_range["50-60"] += occurence
        elif 60 < float(height) < 70:
            mode_data_for_range["60-70"] += occurence
        elif 70 < float(height) < 80:
            mode_data_for_range["70-80"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")