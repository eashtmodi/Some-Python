import csv
import pandas as pd 
import plotly.express as px



with open("class1.csv", newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

print(file_data)

file_data.pop(0)

total_marks=0
frequency=len(file_data)

for data in file_data:
    total_marks=total_marks+float(data[1])

mean=total_marks/frequency
print(mean)

df= pd.read_csv("class1.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=frequency)])
fig.show()

print(df)
