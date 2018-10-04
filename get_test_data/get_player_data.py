import csv
import pandas as pd

csv_file = pd.read_csv("./player_reg_name.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

player_reg=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    player_reg.append(line)
    line = []

#play_reg_data[i][0] #year
#play_reg_data[i][1] #team
#play_reg_data[i][2] #name

csv_file = pd.read_csv("./Player_Regular_Season.csv", header=None, sep=',', skiprows=0, skipinitialspace=True)
file = csv_file.values

player_data=[]
line=[]
for i in range(len(file)):
    for j in range(len(file[i])):
        line.append(file[i][j])
    player_data.append(line)
    line = []

for i in range(len(player_reg)):
    for j in range(len(player_data)):
        if player_data[j][0]+1 == player_reg[i][0]:
            if str(player_data[j][2]) == str(player_reg[i][2]):
                player_reg[i] += player_data[j][5:]
                print(player_reg[i])
                break

new_csv = []
for i in range(0, len(player_reg)):
    new_csv.append(player_reg[i])

file3=csv.writer(open("player_data.csv","w"))
for i in range(len(new_csv)):
    file3.writerow(new_csv[i])



