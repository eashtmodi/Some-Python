import pandas as pd 
import plotly.express as px 
import csv

with open("class2.csv",newline="")  as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

total=0
frequency=len(file_data)

for data in file_data:
    total=total+float(data[1])

mean=total/frequency

print(mean)

df=pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number",y="Marks")


fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=frequency)])
fig.show()