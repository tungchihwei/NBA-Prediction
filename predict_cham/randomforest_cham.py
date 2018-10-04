import csv
import pandas as pd
import numpy as np
from sklearn import cross_validation, ensemble, preprocessing, metrics
import time

start_time = time.time()


#print("woman")
text_file = open("./cham_train_label_19802001.txt", "r")
train_type = text_file.read().split(' ')
#print(len(train_type))
csv_file = pd.read_csv("./cham_train_19802001.csv", header=None, sep=',', skiprows=0, dtype='float', skipinitialspace=True)
train_data_temp = csv_file.values


train_data=[]
train_line=[]
for i in range(len(train_data_temp)):
	for j in range(len(train_data_temp[i])):
		train_line.append(train_data_temp[i][j])
	train_data.append(train_line)
	train_line = []
#print(len(train_data))

csv_file2 = pd.read_csv("./cham_test_20022004.csv", header=None, sep=',', skiprows=0, dtype='float', skipinitialspace=True)
test_data_temp = csv_file2.values

test_data=[]
test_line=[]
for i in range(len(test_data_temp)):
	for j in range(len(test_data_temp[i])):
		test_line.append(test_data_temp[i][j])
	test_data.append(test_line)
	test_line = []

ans_file = open("./cham_test_label_20022004.txt", "r")
ans = ans_file.read().split(' ')

# use sklearn.ensemble's RandomForestClassifier()
forest = ensemble.RandomForestClassifier(n_estimators = 100)
forest.fit(train_data, train_type)
predictions = forest.predict(test_data)

total = len(ans)
count = 0

for i in range(total):
	if predictions[i] == ans[i]:
		count = count + 1

accuracy = (count / total) * 100

print("accuracy: ", accuracy, "%")

print("--- %s seconds ---" % (time.time() - start_time))
