import csv
import pandas as pd

csv_file = pd.read_csv("./playerplayoff_reg.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

playoff_data=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    playoff_data.append(line)
    line = []
# print(playoff_data[1][1])

tmp = []
name = []
year = 1980
count = 0
for i in range(1, 4464):
    # if playoff_data[i][0] == str(year):
    if i != 1:
        if playoff_data[i][1] == playoff_data[i-1][1]:
            name[-1].append(playoff_data[i][2])
        else:
            name.append(playoff_data[i][0:3])
            # print(name)
            # break
    else:
        name.append(playoff_data[i][0:3])


new_csv = []
for i in range(0, len(name)):
	new_csv.append(name[i][0:10])

file3=csv.writer(open("team_playoff_playername.csv","w"))
for i in range(len(new_csv)):
	file3.writerow(new_csv[i])

