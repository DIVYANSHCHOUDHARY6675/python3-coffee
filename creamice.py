import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    icecream=[]
    coldrink=[]
    temprature=[]
    with open (data_path) as dew:
        csvreader=csv.DictReader(dew)
        for i in csvreader:
            icecream.append(float(i["Ice-cream Sales( ₹ )"]))
            temprature.append(float(i["Temperature"]))
    return {"x":temprature,"y":icecream}
def find (data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("the correlation of the data source is"+str(correlation))
def setup ():
   source = getDataSource("icecold.csv")
   find(source)
setup()




