import tflearn
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
import time
import datetime

lenc = LabelEncoder()

final_x = []
final_y = []

files = ['./Datasets/SP1-2016_data.csv', './Datasets/SP1-2015_data.csv', './Datasets/SP1-2014_data.csv', './Datasets/SP1-2013_data.csv', './Datasets/SP1-2012_data.csv']

for f in files:

	data=pd.read_csv(f)

	data['Date'] = pd.to_datetime(data['Date'])

	data = data.sort_values(by='Date', ascending=True)

	y_df = data['HTR']
	x_df = data.loc[:,data.columns != 'HTR']
	y_preprocessed = lenc.fit_transform(np.array(y_df))

	X = np.array(x_df.loc[:,[True if c not in  ['Div','Date','HomeTeam','AwayTeam','HTTeam','ATTeam'] else False for c in x_df.columns]])

	#parsear y
	Y = []
	for y in y_preprocessed:
		if y == 0:
			Y.append([1,0,0])
		elif y == 1:
			Y.append([0,1,0])
		else:
			Y.append([0,0,1])


	for i in range(X.shape[0]):
		if np.any(X[i]):
			final_x.append(X[i])
			final_y.append(Y[i])



X = np.array(final_x)
Y = np.array(final_y)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

num_atributes = X_train.shape[1]

net = tflearn.input_data(shape=[None, num_atributes])
net = tflearn.fully_connected(net, 300, activation="leakyrelu")
net = tflearn.fully_connected(net, 3, activation="leakyrelu")
net = tflearn.regression(net, optimizer= "Nesterov",
                         loss= "categorical_crossentropy", name="output1")
model = tflearn.DNN(net, tensorboard_verbose=2)

# print X_train
# for x in X_train:
# 	print x
# print Y_train
print X_train.shape
print Y_train.shape
model.fit(X_train, Y_train, n_epoch=20, validation_set=0.1, show_metric=True, snapshot_step=100) 

preds = model.predict(X_test)

error = 0.0
for p,y in zip(preds, Y_test):
	if np.nanargmax(p) != np.nanargmax(y):
		error += 1

print ("Error total = " + str(error / len(Y_test)))