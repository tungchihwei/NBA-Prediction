import csv
import pandas as pd

csv_file = pd.read_csv("./player_data.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

player_data=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    player_data.append(line)
    line = []
final = []
team_now = ""
for i in range(len(player_data)):
	if player_data[i][1] != team_now:
		final.append(player_data[i])
		team_now = player_data[i][1]
	else:
		for j in range(14):
			final[-1][j+2] += player_data[i][j+2]


new_csv = []
for i in range(0, len(final)):
    new_csv.append(final[i])

file3=csv.writer(open("test_20022004.csv","w"))
for i in range(len(new_csv)):
    file3.writerow(new_csv[i])
