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


year = 1980
new_csv = []
for i in range(1,len(playoff_data)):

    if int(playoff_data[i][0]) == year:
        if i != 1:
            if playoff_data[i][1] == playoff_data[i-1][1]:
                new_csv[len(new_csv)-1] = new_csv[len(new_csv)-1] + playoff_data[i][2:]
            else:
            	new_csv.append(playoff_data[i])

        else:
            new_csv.append(playoff_data[i])

    else:
        year = year + 1

print(len(new_csv))


file3=csv.writer(open("team_playerplayoff.csv","w"))
for i in range(len(new_csv)):
	file3.writerow(new_csv[i])




#     # print(playoff_data[i][2:])
#     # break
