import csv
import pandas as pd

csv_file = pd.read_csv("./playerplayoff.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

playoff_data=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    playoff_data.append(line)
    line = []