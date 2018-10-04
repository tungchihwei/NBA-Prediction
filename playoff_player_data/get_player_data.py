import csv
import pandas as pd

csv_file = pd.read_csv("./Player_Regular_Season.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

regular_data=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    regular_data.append(line)
    line = []

csv_file = pd.read_csv("./team_playoff_playername.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

player_name=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    player_name.append(line)
    line = []

tmp = []
name = []

for playoff in range(388):
	tmp = []
	count = 0
	for reg in range(11489):
		if player_name[playoff][0] == regular_data[reg][0]:
			if player_name[playoff][1] == regular_data[reg][1]:
				if regular_data[reg][2] in player_name[playoff]:
					tmp = tmp + regular_data[reg][5:]
					count = count + 1
					if count == 6:
						break
					
	tmp = player_name[playoff][0:2] + tmp
	name.append(tmp)

file3=csv.writer(open("playoff_team_champion.csv","w"))
for i in range(len(name)):
	file3.writerow(name[i])