import pandas as pd 
import plotly.express as px

df = pd.read_csv("csv files/data.csv");

fig= px.scatter(df,x="Country",y="InternetUsers");
fig.show();

