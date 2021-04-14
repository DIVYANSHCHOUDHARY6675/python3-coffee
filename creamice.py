import plotly.express as px
import csv
with open ("icecold.csv") as dew:
    df=csv.DictReader(dew)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()
    



