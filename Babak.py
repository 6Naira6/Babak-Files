import pandas as pd
import csv
import os

name= input("Enter file's name: ")
folder= name[9:]
os.mkdir(folder)
folder= folder + "\ "
name= name+".csv"
harbor= pd.read_csv(name)
x, y= harbor.shape
s= 'A'
header= ['IMEI']
for i in range(x):
    s1= harbor.iloc[i][5]
    if (s != s1):
        s= s1
        name= s1 + ".csv"
        name2= name.replace("/"," ")
        name3= folder + name2
        out = open(name3, 'w',  newline='')
        writer = csv.writer(out)
        writer.writerow(header)
    imei= [harbor.iloc[i][2]]
    writer.writerow(imei)
out.close()