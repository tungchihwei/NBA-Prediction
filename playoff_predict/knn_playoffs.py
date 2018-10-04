import csv
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import time

start_time = time.time()

#print("woman")
text_file = open("./playoffs_train_19802001_labels.txt", "r")
train_type = text_file.read().split(' ')
#print(len(train_type))
csv_file = pd.read_csv("./playoffs_train_19802001.csv", header=None, sep=',', skiprows=0, dtype='float', skipinitialspace=True)
train_data_temp = csv_file.values


train_data=[]
train_line=[]
for i in range(len(train_data_temp)):
	for j in range(len(train_data_temp[i])):
		train_line.append(train_data_temp[i][j])
	train_data.append(train_line)
	train_line = []
#print(len(train_data))

csv_file2 = pd.read_csv("./test_20022004.csv", header=None, sep=',', skiprows=0, dtype='float', skipinitialspace=True)
test_data_temp = csv_file2.values

test_data=[]
test_line=[]
for i in range(len(test_data_temp)):
	for j in range(len(test_data_temp[i])):
		test_line.append(test_data_temp[i][j])
	test_data.append(test_line)
	test_line = []

knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(train_data, train_type)
predictions = knn.predict(test_data)


ans_file = open("./playoffs_test_20022004_labels.txt", "r")
ans = ans_file.read().split(' ')

total = len(ans)
count = 0

for i in range(total):
	if predictions[i] == ans[i]:
		count = count + 1

accuracy = (count / total) * 100

print("KNN accuracy: ", accuracy, "%")

print("--- %s seconds ---" % (time.time() - start_time))

